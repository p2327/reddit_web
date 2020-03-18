from flask_mongoengine import MongoEngine


db = MongoEngine()


class Post(db.Document):
    """
    Data model for reddit_top_post collection objects.
    """
    comments_url = db.URLField(required=True)
    date = db.DateTimeField(required=True)
    date_str = db.StringField(max_length=10, required=True)
    score = db.IntField(required=True)
    sub = db.StringField(max_lenght=20, required=True)
    title = db.StringField(max_lenght=300, required=True)
    url = db.URLField(required=True)

    meta = {
        'collection': 'top_reddit_posts',
        'orderting': ['-score'],
        'auto_create_index': False 
    }
