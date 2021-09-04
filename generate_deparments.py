# This script will generate a new departments.json for ttd_helper from tones.cfg for TTD

import configparser
import json
import etc.config as config

parser = configparser.ConfigParser()
parser.read(config.tones_cfg_path)

departments = {}

for tone in parser.sections():
    new_tone = parser[tone]["description"].replace(" ", "_").lower()
    departments[new_tone] = {"mp3_append_file": "", "pushover_app_token": "", "pushover_group_token": "",
                             "mqtt_topic": "dispatch/" + new_tone, "mqtt_message_1": "", "mqtt_message_2": "",
                             "mqtt_interval": 5}

with open('etc/departments.json', 'w') as outfile:
    json.dump(departments, outfile, indent=4)
