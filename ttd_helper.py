import argparse
import os
import lib.zello_handler as zello
import lib.twitter_handler as twitter
import lib.pushover_handler as pushover
import lib.cleanup_handler as cleanup
import lib.mqtt_handler as mqtt
import lib.sftp_handler as sftp
import lib.mp3_handler as mp3
import etc.config as config

parser = argparse.ArgumentParser(description='Process Arguments.')
parser.add_argument("tone_name", help="Tone Name.")
parser.add_argument("mp3", help="MP3 Filepath.")
args = parser.parse_args()

if args.tone_name is not None and args.mp3 is not None:
    mp3_url = config.audio_url + args.mp3.replace("./audio/", "")
    mp3_path = config.ttd_audio_path + "/" + args.mp3.replace("./audio/", "")

    # Mp3 Manipulation In order gain -> stereo -> low pass -> high pass -> append -> normalize
    if config.mp3_gain_settings["enabled"] == 1:
        print("Gain Enabled")
        mp3.gain_filter(mp3_path)
    else:
        print("Not Changing Mp3 Gain")

    if config.mp3_convert_stereo["enabled"] == 1:
        print("MP3 Stereo Convert Enabled")
        mp3.convert_stereo(mp3_path)
    else:
        print("Not Changing Mp3 From Mono")

    if config.mp3_high_pass_settings["enabled"] == 1:
        print("MP3 High Pass Filter Enabled")

        mp3.high_pass_filter(mp3_path)
    else:
        print("Not Filtering Mp3 High Pass")

    if config.mp3_low_pass_settings["enabled"] == 1:
        print("MP3 Low Pass Filter Enabled")
        mp3.low_pass_filter(mp3_path)
    else:
        print("Not Filtering Mp3 Low Pass")

    if config.mp3_append_settings["enabled"] == 1:
        print("MP3 Append Audio Enabled")
        mp3.append_audio(args.tone_name, mp3_path)
    else:
        print("Not Appending Audio to Mp3")

    if config.sftp_settings["enabled"] == 1:
        print("SFTP Enabled")
        # Send file to remote server
        sftp.upload_file(mp3_path)
    else:
        print("Not Sending To SFTP")

    if config.pushover_settings["enabled"] == 1:
        pushover.send_push(args.tone_name, mp3_url)
    else:
        print("Not Sending To Pushover")

    if config.mqtt_settings["enabled"] == 1:
        mqtt.publish_to_mqtt(args.tone_name)
    else:
        print("Not Sending To MQTT")

    if config.twitter_settings["enabled"] == 1:
        print("Twitter Enabled")
        # Post to Twitter
        twitter.send_tweet(config, args.tone_name, mp3_url)
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
