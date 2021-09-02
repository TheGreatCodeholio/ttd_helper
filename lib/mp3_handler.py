from pydub import AudioSegment, silence, effects
import etc.config as config
import json


def convert_stereo(file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = audio1.set_channels(2)
    new_audio.export(file, format="mp3")


def gain_filter(file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = audio1.apply_gain(config.mp3_append_settings["gain_db"])
    new_audio.export(file, format="mp3")


def append_audio(tone_name, file):
    department_name = tone_name.replace(" ", "_").lower()
    json_file = open("../etc/departments.json")
    departments = json.load(json_file)
    if departments:
        if department_name in departments:
            data = departments[department_name]
            audio1 = AudioSegment.from_mp3(file)
            audio2 = AudioSegment.from_mp3(data["mp3_append_file"])
            new_audio = audio2 + audio1
            new_audio.export(file, format="mp3")


def normalize_filter(file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.normalize(audio1)
    new_audio.export(file, format="mp3")


def low_pass_filter(file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.low_pass_filter(audio1, cutoff=config.mp3_low_pass_settings["cutoff"])
    new_audio.export(file, format="mp3")


def high_pass_filter(file):
    audio1 = AudioSegment.from_mp3(file)
    new_audio = effects.high_pass_filter(audio1, cutoff=config.mp3_high_pass_settings["cutoff"])
    new_audio.export(file, format="mp3")
