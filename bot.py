import tweepy
from time import sleep

# Import your Twitter application keys, tokens, and secrets.
consumer_key = 'LPNuizjAsK4t7zvuaZA9cRF9n' 
consumer_secret = 'smYzCkOjtDiyVil8T06BHWmzFUXsbocuUZetkm1tdSCIP9OuXD' 
access_token = '1802318922227884032-q4q5GcrjQq6fObNYJih8ItyGKwvvbN' 
access_token_secret = 'AxAnZXxQGjVzdHRNIGk5fEGC5bp9v4a5ktW7pe1sd0zwe'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPduuQEAAAAA1E4vZn2ZJl195AIsLhFR3Vq%2F14E%3DiLaZCQq1EOQ1cOI10KcsJouTa7zy1X6m93CAO8Ymg6h2xE436o'

# Authentication using OAuth 2.0 Bearer Token
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

# Twitter bot settings for liking Tweets
LIKE = False
# Retweet = True

# Twitter bot settings for following the user who tweeted
FOLLOW = False

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

# Change the hashtags to your choice
query = 'Artificial Intelligence OR AI -is:retweet lang:en'

# Search for tweets using the recent search endpoint
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['author_id']).flatten(limit=100):
    try:
        print('\nTweet by user ID:', tweet.author_id)

        # Retweet the tweet
        client.retweet(tweet.id)
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            client.like(tweet.id)
            print('Liked the tweet')

        # Follow the user who tweeted
        if FOLLOW:
            user = client.get_user(id=tweet.author_id)
            if not user.following:
                client.follow_user(target_user_id=tweet.author_id)
                print('Followed the user')

        # Twitter bot sleep time settings in seconds. Use large delays so that your account will not get banned
        sleep(30)

    except tweepy.TweepyException as e:
        print(e.reason)

    except StopIteration:
        break
