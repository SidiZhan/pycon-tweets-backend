import redis

from flask import Flask, g, request, jsonify, make_response
from datetime import datetime
from json import dumps,loads

app = Flask(__name__)
myTweets = []

DB_HOST = 'redis'
DB_PORT = 6379
DB_NO = 0

def init_db():
    db = redis.StrictRedis(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NO)
    return db

@app.before_request
def before_request():
    g.db = init_db()

@app.route('/')
def index():
    g.db.incr('hits')
    return 'Pycon tweets sddtc has been viewed %s time(s).' % g.db.get('hits')

@app.route('/<username>/tweet', methods=['POST'])
def add_tweet(username):
    tweet_content = request.json['tweet_content']
    tweet = {'username': username, 'content': tweet_content, 'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}
    myTweets.append(tweet)

    response = make_response(jsonify(tweet))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response, 200

@app.route('/<username>/tweets', methods=['GET'])
def list_tweets(username):

    response = make_response(dumps(myTweets))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
