import os

from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import sys
import etc.config as config


def upload_file(file):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(config.sftp_settings["sftp_host"], port=config.sftp_settings["sftp_port"],
                username=config.sftp_settings["sftp_user"], password=config.sftp_settings["sftp_pass"])

    scp = SCPClient(ssh.get_transport(), progress=progress)
    scp.put(file, remote_path=config.sftp_settings["remote_path"])

# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent) / float(size) * 100))


def clean_remote_files():
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(config.sftp_settings["sftp_host"], port=config.sftp_settings["sftp_port"],
                username=config.sftp_settings["sftp_user"], password=config.sftp_settings["sftp_pass"])
    command = "find " + config.sftp_settings["remote_path"] + "* -mtime +" + str(config.remote_cleanup_settings["cleanup_days"]) + " -exec rm {} \;"
    stdin, stdout, stderr = ssh.exec_command(command)
    for line in stdout:
        # Process each line in the remote output
        print(str(line))

