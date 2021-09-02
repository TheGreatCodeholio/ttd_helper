# TTD Helper
Python script to add functionality to TTD.  Designed for Python 3.7+ Raspberry Pi 3 or 4.

## Raspberry Pi Dependancies
- Opus Tools
   - sudo apt install opus-tools

## Python 3 Dependencies
- paramiko~=2.6.0
- scp~=0.13.6
- aiohttp~=3.7.4.post0
- crypto~=1.4.1
- TwitterAPI~=2.7.3
- requests~=2.25.1

## Installation
- Open Terminal window
- In home folder clone this repository
  - `git clone https://github.com/TheGreatCodeholio/ttd_helper.git`
- Change to the ttd_helper directory
  - `cd ttd_helper` 
- Change ttd_helper.sh permissions to allow execution
  - `chmod a+x ttd_helper.sh`
- Copy ttd_helper.sh to TTD directory
  - `cp ttd_helper.sh /home/pi/TTD`
- `pip3 install -r requirements.txt`
- `sudo apt install opus-tools`
- Copy departments_sample.json to departments.json (See /etc/departments.json notes)
  - `cp etc/departments_sample.json etc/departments.json`
- Copy config_sample.py to config.py (See /etc/config.py notes)
  - `cp etc/config_sample.py etc/config.py`

## Running
To run the script configure TTD to ttd_helper.sh for your Tone
- Post-email Command: ./ttd_helper.sh "[d]" [mp3]
  - on this line we pass [d] (department/tone name), [mp3] (mp3 filename)
- This will run the command once the tone has been processed and emails have been sent. 

## Functions:
- Manipulate TTD MP3 with filters, gain, or append audio file to the beginning.
- Upload TTD audio file to SFTP server
- Send Notification via Pushover
- Send a tweet via Twitter
- Stream audio to Zello
- Clean up old local and remote audio files
- Publish to MQTT Topic

## MP3 Manipulation
Modify the MP3 that was output by TTD. 
- Gain level 
- Convert to Stereo
- High Pass Filter
- Low Pass Filter
- Append another audio file to the beginning based on tone decoded.
  - file to append is determined in the "/etc/departments.json" settings for each tone
- Normalize Filter

## SFTP Upload
This is Required if you will be using the Twitter or Pushover functions. You will need the audio uploaded to a remote webserver where it can be accessed by a URL.
- Your user will need proper permission on the folder you are sending the audio file to.
- In my case I have the sftp user owning the folder /var/www/html/audio and www-data as the group and 775 permissions to make it writable as the sftp user.

## MQTT Topic Publish
This function will Publish one or two messages to a MQTT topic by connecting to a broker.
- MQTT requires your tone name in the department.json and the settings set to your preferences. See the file for the formatting. Example: If your TTD Tone name is "Example Fire Department" the json block would start with "example_fire_department"

## Twitter:
Request API access for you account https://developer.twitter.com
Once you have access you will need four tokens.
- API Consumer Key and Secret
- API Access Token and Secret
- Those will be placed in etc/config.py

## Pushover:
Create a Application and group for each department.
You will need to add each  Application and groups token to the departments.json for each tone/department 

## Zello
Create a developer account with Zello to get credentials.  Set up a different account than what you normally use for Zello, as trying to use this script with the same account that you're using on your mobile device will cause problems.

For Zello consumer network:
- Go to https://developers.zello.com/ and click Login
- Enter your Zello username and password. If you don't have Zello account download Zello app and create one.
- Complete all fields in the developer profile and click Submit
- Click Keys and Add Key
- Copy and save Sample Development Token, Issuer, and Private Key. Make sure you copy each of the values completely using Select All.
- Click Close
- Copy the contents of the Private Key into a /etc/config.py.
- The Issuer value goes into /etc/config.py.
- The Account username and password also goes in /etc/config.py

## File Cleanup
This will clean up local or remote audio files older than x days as set in /etc/config.py
- Two separate configuration sections "local" and "remote"
- Can be enabled so local is cleaned and remote isn't or vise versa or not cleaned at all

## /etc/config.py
Copy config_sample.py to config.py 
  - `cp config_sample.py config.py`
  - audio_url:  Base URL path for your audio files. Example https://example.com/audio
  - ttd_audio_path:  The path to TTD audio folder. Example /home/pi/TTD/audio (no slash at the end)  
  - local_cleanup_settings:  Settings for local cleanup
    - enabled: 1 or 0 (On/Off)
    - cleanup_days: 7 (Number of days to keep old files before deleting)
  - remote_cleanup_settings:  Settings for remote cleanup (SFTP Server)
    - enabled: 1 or 0 (On/Off)
    - cleanup_days: 7 (Number of days to keep old files before deleting)
  - mp3_gain_settings: The settings for MP3 Gain Manipulation
    - enabled: 1 or 0 (On/Off)
    - gain_db: db to increase audio volume
  - mp3_convert_stereo: Converts MP3 to Stereo from Mono
    - enabled: 1 or 0 (On/Off)
  - mp3_high_pass_settings: The settings for MP3 High Pass Filter
    - enabled: 1 or 0 (On/Off)
    - cutoff: hz for high pass cutoff
  - mp3_low_pass_settings: The settings for MP3 Low Pass Filter
    - enabled: 1 or 0 (On/Off)
    - cutoff: hz for low pass cutoff
  - mp3_append_settings: The settings for appending another MP3 to the beginning of the audio
    - enabled: 1 or 0 (On/Off)
  - mp3_normalize_settings: The setting to normalize the audio for the MP3
    - enabled: 1 or 0 (On/Off)
  - sftp_settings: The settings for SFTP upload
    - enabled: 1 or 0 (On/Off)
    - remote_path: This is the remote path to upload to. Example /var/www/html/audio
    - sftp_user: stfp username
    - sftp_pass: stfp password
    - sftp_host: sftp hostname Example: example.com
    - sftp_port: sftp port number Example: 22
    - delete_after_upload: 1 or 0 (On/Off) Deletes MP3 file after uploading to SFTP
  - pushover_settings:  Settings for Pushover function
    - enabled: 1 or 0 (On/Off)
  - mqtt_settings : Settings for MQTT Function
    - enabled: 1 or 0 (On/Off)
    - mqtt_host: MQTT Hostname or IP address
    - mqtt_port: MQTT Port number
    - mqtt_pusername: MQTT Username
    - mqtt_password: MQTT Password
  - zello_settings:  Settings for Zello upload
    - enabled: 1 or 0 (On/Off)
    - delete_after_stream: 1 or 0 (On/Off) Deletes opus file after streaming to Zello
    - username: Zello Username
    - password: Zello Password
    - token: Zello API token
    - issuer: Issuer credential from Zello account (see above Zello Section)
    - private_key: Private Key from Zello Development copied between two sets of triple quotes """HERE""""
  - twitter_settings: Settings for Twitter Tweets
    -  enabled: 1 or 0 (On/Off)
    -  consumer_key: API Consumer Key
    -  consumer_secret: API Consumer Secret Key
    -  access_token: API Access Token Key
    -  access_token_secret: API Access Token Secret Key 

## /etc/departments.json
Copy departments_sample.json to departments.json 
  - `cp departments_sample.json departments.json`
This file is like the tones.cfg for TTD. If requires each department/tone to be configured within it.

### Settings for each tone/department:
- mp3_append_file: Full path to an MP3 file to add to the beginning of the MP3 file from TTD
- pushover_app_token: This is the API token for the application created in Pushover. (Each Tone requires and Application and Group in Pushover)
- pushover_group_token: This is the Group Token for the group that your application is sending messages to.
- mqtt_topic: The MQTT Topic name to publish to for this department.
- mqtt_message_1: The message to publish to the mqtt_topic
- mqtt_message_2: The second message to publish to the mqtt topic (if set to "" it will skip publishing a second message, useful to turn switches/relays off after a interval)
- mqtt_interval: If a second message is set this is the interval in seconds between message1 and message 2.