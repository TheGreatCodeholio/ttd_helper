import requests
import etc.config as config
import json


def send_push(tone_name, audio_link):
    message_string = """<font color="red"><b>{}</b></font>

    <a href="{}">Click for Dispatch Audio</a>
    """
    department_name = tone_name.replace(" ", "_").lower()
    json_file = open("../etc/departments.json")
    departments = json.load(json_file)
    if departments:
        if department_name in departments:
            data = departments[department_name]
            r = requests.post("https://api.pushover.net/1/messages.json", data={
                "token": data["pushover_app_token"],
                "user": data["pushover_group_token"],
                "html": 1,
                "message": message_string.format(department_name, audio_link)
            })
            print(r.text)
