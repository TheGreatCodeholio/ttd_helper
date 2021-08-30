#!/usr/bin/python

from TwitterAPI import TwitterAPI


def send_tweet(config, department_name, mp3_link):
    tweet_status = "Dispatch Alert\n" + department_name + "\n" + mp3_link
    api = TwitterAPI(config.twitter_settings["consumer_key"], config.twitter_settings["consumer_secret"],
                     config.twitter_settings["access_token"], config.twitter_settings["access_token_secret"])
    r = api.request('statuses/update', {'status': tweet_status})