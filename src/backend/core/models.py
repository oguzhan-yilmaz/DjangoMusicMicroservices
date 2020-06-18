from django.db import models

from django.contrib.auth.models import AbstractUser
from .utils import decode_np_arr, encode_np_arr, in_seconds_frame
from django.dispatch import receiver
import os
import numpy as np
from .utils import load_audio
from essentia import standard as es
from .utils import annotate_song

class User(AbstractUser):
    # this should extend the base user model

    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')


def upload_song_to(instance, filename):
    return 'static/music_files/%s/%s' % (instance.user.username, filename)

class SongModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    song_file = models.FileField(
        upload_to=upload_song_to, null=True, blank=True)
    song_title = models.CharField(max_length=300, null=True)
    bpm = models.IntegerField(null=True)
    key = models.CharField(max_length=2, null=True)
    key_scale = models.CharField(max_length=5, null=True)
    key_strength = models.FloatField(null=True)

    def __str__(self):
        return self.song_title or "song"


# Django signals

@receiver(models.signals.post_save, sender=SongModel)
def auto_session_and_controller_create_for_user(sender, instance, created, **kwargs):
    # if this is the creation of the user model, do 
    def get_song_name_and_format(filepath):
        # returns ../song_name.format -> song_name and song_format
        return filepath.split('/')[-1].split('.')

    if created:
        # annotate song
        music_file_path = instance.song_file.path
        annotation = annotate_song(music_file_path)
        song_title, song_format = get_song_name_and_format(music_file_path)
        instance.song_title = song_title
        instance.bpm = annotation['bpm']
        instance.key = annotation['key']
        instance.key_strength = annotation['key_strength']
        instance.key_scale = annotation['key_scale']
        instance.save()

@receiver(models.signals.post_delete, sender=SongModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem when corresponding SongModel object is deleted.
    """
    file = instance.song_file

    if file:
        if os.path.isfile(file.path):
            os.remove(file.path)