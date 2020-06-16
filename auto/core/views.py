from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .forms import SongFileUploadForm
from django.views.generic.edit import FormView
from .models import *
# Create your views here.
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
            annotate_song_and_partition_it(sm)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class SongModelListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        # TODO MAKE a prefetch
        songs = SongModel.objects.filter(user=request.user)
        serializer = SongModelSerializer(songs, many=True)
        return Response(serializer.data)