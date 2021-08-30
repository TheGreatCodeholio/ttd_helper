import os
import time
import etc.config as config


def cleanup_local_audio():
    current_time = time.time()
    for f in os.listdir(config.ttd_audio_path):
        path = os.path.join(config.ttd_audio_path + "/", f)
        creation_time = os.path.getctime(path)
        if (current_time - creation_time) // (24 * 3600) >= config.local_cleanup_settings["cleanup_days"]:
            os.unlink(path)
            print('{} removed'.format(path))
            print("\n")
