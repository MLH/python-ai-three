import config
import tweepy


# user authentication to use twitter API
def get_user_auth_twitter():
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return auth


# fetch tweets
def get_user_tweets(twitter_handle):
    auth = get_user_auth_twitter()
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(
        twitter_handle, count=(config.NUM_TWEETS_TO_GRAB or 100), tweet_mode="extended"
    )


    return [tweet._json["full_text"] for tweet in public_tweets]
