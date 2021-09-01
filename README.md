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
- copy ttd_helper.sh to TTD directory
  - `cp ttd_helper.sh /home/pi/TTD`
- `pip3 install -r requirements.txt`
- `sudo apt install opus-tools`

## Running
To run the script configure TTD to ttd_helper.sh for your Tone
- Post-email Command: ./ttd_helper.sh "[d]" [mp3] 0
  - on this line we pass [d] (department name), [mp3] (mp3 filename), and pushbullet group token (0 if you are not using pushbullet or don't have a group for that tone) 
- This will run the command once the tone has been processed and emails have been sent. 

## Functions:
- Upload TTD audio file to SFTP server
- Send Notification via Pushover
- Send a tweet via Twitter
- Stream audio to Zello
- Clean up old local and remote audio files

## SFTP Upload
This is Required if you will be using the Twitter or Pushover functions. You will need the audio uploaded to a remote webserver where it can be accessed by a URL.
- Your user will need proper permission on the folder you are sending the audio file to.
- In my case I have the sftp user owning the folder/var/www/html/audio and www-data as the group and 775 permissions to make it writable as the sftp user.

## Twitter:
Request API access for you account https://developer.twitter.com
Once you have access you will need four tokens.
- API Consumer Key and Secret
- API Access Token and Secret
- Those will be placed in etc/config.py

## Pushover:
Create a Application and group for each department.
You will need each groups token as a paramater when telling TTD to run the helper script

##Zello
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
- Two seperate configuration sections "local" and "remote"
- Can be enabled so local is cleaned and remote isn't or vise versa or not cleaned at all

## /etc/config.py
- audio_url:  Base URL path for your audio files. Example https://example.com/audio
- ttd_audio_path:  The path to TTD audio folder. Example /home/pi/TTD/audio (no slash at the end)  
- local_cleanup_settings:  Settings for local cleanup
  - enabled: 1 or 0 (On/Off)
  - cleanup_days: 7 (Number of days to keep old files before deleting)
- remote_cleanup_settings:  Settings for remote cleanup (SFTP Server)
  - enabled: 1 or 0 (On/Off)
  - cleanup_days: 7 (Number of days to keep old files before deleting)
- sftp_settings: The settings for SFTP upload
  -  enabled: 1 or 0 (On/Off)
  -  remote_path: This is the remote path to upload to. Example /var/www/html/audio
  -  sftp_user: stfp username
  -  sftp_pass: stfp password
  -  sftp_host: sftp hostname Example: example.com
  -  sftp_port: sftp port number Example: 22
- pushover_settings:  Settings for Pushover function
  - enabled: 1 or 0 (On/Off)
  - token: Pushover API token
- zello_settings:  Settings for Zello upload
  -  enabled: 1 or 0 (On/Off)
  -  username: Zello Username
  -  password: Zello Password
  -  token: Zello API token
  -  issuer: Issuer credential from Zello account (see above Zello Section)
  -  private_key: Private Key from Zello Development copied between two sets of triple quotes """HERE""""
- twitter_settings: Settings for Twitter Tweets
  -  enabled: 1 or 0 (On/Off)
  -  consumer_key: API Consumer Key
  -  consumer_secret: API Consumer Secret Key
  -  access_token: API Access Token Key
  -  access_token_secret: API Acess Token Secret Key 