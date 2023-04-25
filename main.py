import requests
from requests_oauthlib import OAuth1
import os
import json
import random

# Define the tokens and keys by using environment variables (wouldn't want the bot to get hacked lol)
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

def get_random_dialogue():
    # This function chooses one random dialogue line from the Aranara dialogue pool and returns it
    # Entry parameters: No entry parameters
    # Output: Returns a random line of dialogue said by an aranara
    dialogue = []

    with open('aranara_lines_ES.jsonl', 'r', encoding="utf8") as f: # Read the jsonl file with the dialogue lines and choose a random one
        lines = f.readlines()
        random_line = random.choice(lines)
        dialogue_line = json.loads(random_line)

    return dialogue_line[0]

def format_dialogue_line(dialogue_line):
   return {"text": "{}".format(dialogue_line)}

def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
   auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth

def post_tweet():
   dialogue_line = get_random_dialogue()
   payload = format_dialogue_line(dialogue_line)

   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_token_secret
   )

   request = requests.post(
       auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
   )

   print(request.text)

post_tweet()