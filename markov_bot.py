                    ##write code here!!!
import config
import random
from tweepy_fetcher import get_user_tweets as fetch
from twitter_scraper_fetcher import get_user_tweets as scrape
import re


# remove emoji, punctuation, urls from tweets
def clean_tweets_data(tweets):
    text = ""

    # remove emoji from tweets:
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    url_pattern = re.compile(r"http\S+", re.DOTALL)
    mentions_pattern = re.compile(r"@\S+", re.DOTALL)

    # return tweet
    for tweet in tweets:
        # workaround to get full_text from tweepy (otherwise text is truncated)
        text_without_emoji = emoji_pattern.sub(r"", tweet)
        text_without_url = url_pattern.sub(r"", text_without_emoji)
        cleaned_text = mentions_pattern.sub(r"", text_without_url)
        text += (
            text_without_emoji + "\n\n"
        )  # Make sure each tweet is handled properly by markovify

    return text


def generate_bot_answer_with_text_model(user_question, text_model):
    
    
    
    
    
    
    
    
    
    
    
    
         

# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    tweets = fetch(twitter_handle)
    parsed_text = clean_tweets_data(tweets)
    ##write code here!!
    