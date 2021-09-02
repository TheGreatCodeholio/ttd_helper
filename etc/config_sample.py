audio_url = "https://example.com"
ttd_audio_path = "/home/pi/TTD/audio"

local_cleanup_settings = {
    "enabled": 0,
    "cleanup_days": 7
}
remote_cleanup_settings = {
    "enabled": 0,
    "cleanup_days": 7
}

mp3_gain_settings = {
    "enabled": 0,
    "gain_db": 10
}

mp3_convert_stereo = {
    "enabled": 0,
}

mp3_high_pass_settings = {
    "enabled": 0,
    "cutoff_freq": 1000
}

mp3_low_pass_settings = {
    "enabled": 0,
    "cutoff_freq": 1000
}

mp3_append_settings = {
    "enabled": 0
}

mp3_normalize_settings = {
    "enabled": 0,
}

sftp_settings = {
    "enabled": 0,
    "remote_path": "/var/www/html/audio",
    "sftp_user": "user",
    "sftp_pass": "password",
    "sftp_host": "example.com",
    "sftp_port": 22,
    "delete_after_upload": 0
}

pushover_settings = {
    "enabled": 0,
}

mqtt_settings = {
    "enabled": 0,
    "mqtt_host": "localhost",
    "mqtt_port": 1883,
    "mqtt_username": "username",
    "mqtt_password": "test1234"
}

zello_settings = {
    "enabled": 0,
    "username": "ZelloUser",
    "password": "ZelloPass",
    "token": "ZelloToken",
    "channel": "ZelloChannel",
    "issuer": "PRIVATE KEY ISSUER",
    "private_key": """---PRIVATE KEY FROM ZELLO"""
}

twitter_settings = {
    "enabled": 0,
    "consumer_key": "twitter_consumer_key",
    "consumer_secret": "twitter_secret_key",
    "access_token": "twitter_access_token",
    "access_token_secret": "twitter_private_token"
}
