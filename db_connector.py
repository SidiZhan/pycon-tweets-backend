import redis

DB_HOST = 'redis'
DB_PORT = 6379
DB_NO = 0

def init_db():
    db = redis.StrictRedis(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NO)
    return db
