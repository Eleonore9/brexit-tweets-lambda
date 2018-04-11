import twitter
import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def get_brexit_tweets(ck, cs, tk, ts):
    api = twitter.Api(consumer_key=ck,
                      consumer_secret=cs,
                      access_token_key=tk,
                      access_token_secret=ts)

    brexit_tweets = api.GetSearch(term="brexit")
    return brexit_tweets

def parse_tweets(tweets):
    list_tweets = [{"created_at": t.created_at,
                    "timezone": t.user.time_zone,
                    "text_content": t.text,
                    "is_truncated": t.truncated,
                    "favorites": t.favorite_count,
                    "retweets": t.retweet_count}
                   for t in tweets]
    return list_tweets


if __name__ == '__main__':
    try:
        c_key = os.environ['CONSUMER_KEY']
        c_secret = os.environ['CONSUMER_SECRET']
        t_key = os.environ['ACCESS_TOKEN_KEY']
        t_secret = os.environ['ACCESS_TOKEN_SECRET']
    except KeyError as e:
        print('ERROR: Please define environment variables consumer_key, consumer_secret, access_token_key, access_token_secret.')
        exit(1)

    #tw = get_brexit_tweets(c_key, c_secret, t_key, t_secret)
    #parsed_tw = parse_tweets(tw)
    #print("I have retrieved {} brexit tweets".format(len(parsed_tw)))
