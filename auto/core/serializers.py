from rest_framework import serializers
from .models import SongModel, User
from rest_framework import viewsets, renderers

class UserSerializer(serializers.ModelSerializer):
    user_songs = serializers.SerializerMethodField()

    def get_user_songs(self, obj):
        song_queryset = SongModel.objects.filter(user=obj)
        return SongModelSerializer(song_queryset, many=True).data

    class Meta:
        model = User
        fields = ['id', 'username', 'user_songs']

class SongModelSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        domain = 'http://localhost:8000/'  # current_site.domain
        path = obj.song_file.url
        print(path)
        return domain + path
    class Meta:
        model = SongModel
        fields = ['id', 'song_title', 'bpm',
                  'key', 'key_scale', 'url']