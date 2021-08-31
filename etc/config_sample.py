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

sftp_settings = {
    "enabled": 0,
    "remote_path": "/var/www/html/audio",
    "sftp_user": "user",
    "sftp_pass": "password",
    "sftp_host": "example.com",
    "sftp_port": 22
}

pushover_settings = {
    "enabled": 0,
    "token": "pushover-api-token"
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
