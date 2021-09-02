import argparse
import os
import lib.zello_handler as zello
import lib.twitter_handler as twitter
import lib.pushover_handler as pushover
import lib.cleanup_handler as cleanup
import lib.mqtt_handler as mqtt
import lib.sftp_handler as sftp
import etc.config as config

parser = argparse.ArgumentParser(description='Process Arguments.')
parser.add_argument("tone_name", help="Tone Name.")
parser.add_argument("mp3", help="MP3 Filepath.")
args = parser.parse_args()

if args.tone_name is not None and args.mp3 is not None:
    call_mp3 = config.audio_url + args.mp3.replace("./audio/", "")
    # Debug show MP3 URL in Console

    if config.sftp_settings["enabled"] == 1:
        print("SFTP Enabled")
        # Send file to remote server
        sftp.upload_file(config.ttd_audio_path + "/" + args.mp3.replace("./audio/", ""))
    else:
        print("Not Sending To SFTP")

    if config.pushover_settings["enabled"] == 1:
        pushover.send_push(args.tone_name, call_mp3)
    else:
        print("Not Sending To Pushover")

    if config.mqtt_settings["enabled"] == 1:
        mqtt.publish_to_mqtt(args.tone_name)
    else:
        print("Not Sending To MQTT")

    if config.twitter_settings["enabled"] == 1:
        print("Twitter Enabled")
        # Post to Twitter
        twitter.send_tweet(config, args.tone_name, call_mp3)
    else:
        print("Not Sending To Twitter")

    if config.zello_settings["enabled"] == 1:
        # Debug to Console
        print("Zello Enabled")
        config.token = zello.zello_create_token(config)
        opus_file = zello.zello_convert(config.ttd_audio_path, args.mp3.replace("./audio/", "").replace(".mp3", ""))
        zello.ZelloSend(config, opus_file).zello_init_upload()
        if os.path.exists(opus_file):
            os.remove(opus_file)
    else:
        print("Not Sending To Zello")

    if config.local_cleanup_settings["enabled"] == 1:
        print("Cleaning Local Files")
        cleanup.cleanup_local_audio()
    else:
        print("Not Cleaning Local")

    if config.remote_cleanup_settings["enabled"] == 1:
        print("Cleaning Remote Files")
        sftp.clean_remote_files()
    else:
        print("Not Cleaning Remote")
