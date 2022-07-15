from operator import truediv
import tweepy
from ssm_secrets import get_secret

client = tweepy.Client(
    consumer_key=get_secret("CONSUMER_KEY"),
    consumer_secret=get_secret("CONSUMER_SECRET"),
    access_token=get_secret("ACCESS_TOKEN_KEY"),
    access_token_secret=get_secret("ACCESS_TOKEN_SECRET")
)


def search_tweets(stock):
    res = client.search_recent_tweets(stock, max_results=100, user_auth=True)
    return res


def handler(event, context):
    res = search_tweets('mirza int')
    # print(res)

    filtered = list(filter(parse_data, res.data))
    print(filtered)


def parse_data(text):
    if "break out" in text:
        return True
    else:
        return False
