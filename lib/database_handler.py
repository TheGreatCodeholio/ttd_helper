# Python Core
import json

# Python 3rd Party
import time
import mysql.connector as mysql

# Project Libraries
import etc.config as config


class Database:
    def __init__(self):
        self.connection = mysql.connect(
            host=config.mysql_settings["mysql_host"],
            user=config.mysql_settings["mysql_username"],
            password=config.mysql_settings["mysql_password"],
            database=config.mysql_settings["mysql_database"],
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def add_new_call(self, tone_name, mp3_url):
        query = "INSERT INTO ttd_calls (call_tone_name, call_mp3_url) VALUES (%s, %s)"
        self.cursor.execute(query, (tone_name, mp3_url))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()