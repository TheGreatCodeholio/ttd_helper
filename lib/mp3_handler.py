from pydub import AudioSegment, effects
import pyttsx3
import os
import etc.config as config
import json


def append_audiotext(tone_name, file):
    engine = pyttsx3.init()
    engine.save_to_file(tone_name, config.ttd_audio_path + "/" + "dept_name.mp3")
    engine.runAndWait()
    audio1 = AudioSegment.from_mp3(file)
    audio2 = AudioSegment.from_mp3(config.ttd_audio_path + "/" + "dept_name.mp3")
    new_audio = audio2 + audio1
    new_audio.export(file, format="mp3", tags={'artist': tone_name})
    if os.path.exists(config.ttd_audio_path + "/" + "dept_name.mp3"):
        os.remove(config.ttd_audio_path + "/" + "dept_name.mp3")


def convert_stereo(tone_name, file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = audio1.set_channels(2)
    new_audio.export(file, format="mp3", tags={'artist': tone_name})


def gain_filter(tone_name, file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = audio1.apply_gain(config.mp3_gain_settings["gain_db"])
    new_audio.export(file, format="mp3", tags={'artist': tone_name})


def append_audio(tone_name, file):
    department_name = tone_name.replace(" ", "_").lower()
    json_file = open("etc/departments.json")
    departments = json.load(json_file)
    if departments:
        if department_name in departments:
            data = departments[department_name]
            if data["mp3_append_file"] is not None and data["mp3_append_file"] != '':
                audio1 = AudioSegment.from_mp3(file)
                audio2 = AudioSegment.from_mp3(data["mp3_append_file"])
                new_audio = audio2 + audio1
                new_audio.export(file, format="mp3", tags={'artist': tone_name})


def normalize_filter(tone_name, file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.normalize(audio1)
    new_audio.export(file, format="mp3", tags={'artist': tone_name})


def low_pass_filter(tone_name, file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.low_pass_filter(audio1, cutoff=config.mp3_low_pass_settings["cutoff_freq"])
    new_audio.export(file, format="mp3", tags={'artist': tone_name})


def high_pass_filter(tone_name, file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.high_pass_filter(audio1, cutoff=config.mp3_high_pass_settings["cutoff_freq"])
    new_audio.export(file, format="mp3", tags={'artist': tone_name})
