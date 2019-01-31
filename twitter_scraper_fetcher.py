import requests
from bs4 import BeautifulSoup
import re

CONTENT_CLASS_NAME = "TweetTextSize"
CONTENT_CONTAINER_TAGS = ["p"]
EMPTY_ITEMS = [None, "", "None"]

TWITTER_URL = "https://twitter.com/"


def get_elements(twitter_handle):
    # Get HTML content from twitter profile page
    url = TWITTER_URL + twitter_handle
    response = requests.get(url)
    html = response.content

    # handles HTML entities
    soup = BeautifulSoup(html, features="html.parser")

    # Find tweets usign class name
    return soup.find_all(CONTENT_CONTAINER_TAGS, attrs={"class": CONTENT_CLASS_NAME})


def get_user_tweets(twitter_handle):
    elements = get_elements(twitter_handle)
    tweets = []

    for post in elements:
        for text in post.contents:
            # check if line contains real text
            if text.string not in EMPTY_ITEMS:
                tweets.append(text.string)

    return tweets
