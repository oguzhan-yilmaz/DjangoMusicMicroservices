import base64
import pickle
import numpy as np
from essentia import standard as es

def annotate_song(filepath):

    audio = load_audio(filepath)
    key, scale, key_strength = es.KeyExtractor(profileType='edma')(audio)
    key_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # transforming bemol to sharp
    if len(key) == 2 and key[1] == 'b':
        cur_idx = key_list.index(key[0])
        new_idx = (cur_idx - 1) % len(key_list)
        new_key = key_list[new_idx] + '#'
        key = new_key

    # for calculating bpm, its proven that RhythmExtractor2013 works best but takes longer
    rhythm_desc = es.RhythmExtractor2013()(audio)
    bpm = round(rhythm_desc[0])
    del audio
    return {'bpm': bpm,
            'key': key,
            'key_scale': scale,
            'key_strength': key_strength,
            'beats': beats}

def in_seconds(seconds):
    # returns a string that gives out given seconds as mins:secs
    return "{}:{}".format(int(seconds // 60), str(int(seconds % 60)).zfill(2))


def load_audio(filepath):
    # returns loaded mono audio.
    from essentia.standard import MonoLoader
    audio = MonoLoader(filename=filepath)()
    return audio


def in_seconds_frame(frames):
    seconds = frames // 44100
    return "{}:{}".format(int(seconds // 60), str(int(seconds % 60)).zfill(2))


def encode_np_arr(arr):
    arr_pickled = pickle.dumps(arr)
    arr_b64 = base64.b64encode(arr_pickled)
    return arr_b64


def decode_np_arr(arr_b64):
    arr_bytes = base64.b64decode(arr_b64)
    unpickled_arr = pickle.loads(arr_bytes)
    return unpickled_arr

def base_65_encode(arr):
    return base64.b64encode(arr)