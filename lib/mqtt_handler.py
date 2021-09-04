import time

import paho.mqtt.client as mqtt
import etc.config as config
import json


def on_disconnect(client, userdata, rc):
    print("client disconnected ok")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


def on_publish(client, userdata, result):
    print("data published \n")
    pass


def publish_to_mqtt(tone_name):
    department_name = tone_name.replace(" ", "_").lower()
    json_file = open("etc/departments.json")
    departments = json.load(json_file)
    if departments:
        if department_name in departments:
            data = departments[department_name]
            if data["mqtt_message_1"] is not None and data["mqtt_topic"] is not None:
                mqtt_client = mqtt.Client()
                mqtt_client.on_connect = on_connect
                mqtt_client.on_publish = on_publish
                mqtt_client.on_disconnect = on_disconnect
                mqtt_client.loop_start()
                mqtt_client.connected_flag = False
                mqtt_client.username_pw_set(config.mqtt_settings["mqtt_username"], config.mqtt_settings["mqtt_password"])
                print("Connecting to broker ", config.mqtt_settings["mqtt_host"])
                mqtt_client.connect(config.mqtt_settings["mqtt_host"], config.mqtt_settings["mqtt_port"])
                while not mqtt_client.connected_flag:  # wait in loop
                    time.sleep(1)
                    print("In wait loop")
                print("In main loop")
                mqtt_client.publish(data["mqtt_topic"], data["mqtt_message_1"])
                if data["mqtt_message_2"] is not None:
                    time.sleep(data["mqtt_interval"])
                    mqtt_client.publish(data["mqtt_topic"], data["mqtt_message_2"])
                mqtt_client.loop_stop()
                mqtt_client.disconnect()
    json_file.close()
