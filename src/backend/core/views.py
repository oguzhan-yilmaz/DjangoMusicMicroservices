from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .forms import SongFileUploadForm
from django.views.generic.edit import FormView
from .models import *
from .serializers import *
# Create your views here.

def homepage(request):
    context = {}
    if request.user.is_authenticated:
        songs = SongModel.objects.filter(user=request.user)
        serializer = SongModelSerializer(songs, many=True)
        context.update({'songs':serializer.data}) 

    return render(request, 'core/homepage.html', context)
class SongUploadView(FormView):
    form_class = SongFileUploadForm
    template_name = 'core/song_upload.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        annotated_songs = SongModel.objects.filter(user=self.request.user.id)
        data['annotated_songs'] = annotated_songs
        return data

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['file']
        if form.is_valid():
            # TODO: Create song obj here.
            print('creating song in form view...')
            user = request.user
            music_file = file
            sm = SongModel(song_file=music_file, user=user)
            sm.save()
            print('upload complete, starting annotating')
            # here

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserApiView(APIView):

    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email', None)
        user_username = request.data.get('username', None)
        user_password = request.data.get('password', None)
        if user_email is None or user_password is None or user_username is None:
            return Response({'detail': 'Email, Username or Password fields must be not empty.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if not validateEmail(user_email):
                return Response({'detail': 'Please enter a valid email.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # valid email.
                # TODO: add more fields
                user = User.objects.create(
                    email=user_email, username=user_username)
                user.set_password(user_password)
                user.is_active = False
                user.save()
                s_user = UserSerializer(user)
                return Response(s_user.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        s_user = UserSerializer(request.user)
        return Response(s_user.data)


class SongModelListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        # TODO MAKE a prefetch
        songs = SongModel.objects.filter(user=request.user)
        serializer = SongModelSerializer(songs, many=True)
        return Response(serializer.data)