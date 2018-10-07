import redis

from flask import Flask
from flask import g

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
