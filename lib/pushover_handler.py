import requests
import etc.config as config


def send_push(department_name, audio_link, group_token):
    message_string = """<font color="red"><b>{}</b></font>

    <a href="{}">Click for Dispatch Audio</a>
    """
    r = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": config.pushover_settings["token"],
        "user": group_token,
        "html": 1,
        "message": message_string.format(department_name, audio_link)
    })
    print(r.text)
