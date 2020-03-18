from flask import Flask, render_template
from models import db, Post


MONGO_URI = 'mongodb+srv://pete:d71RZ9Xu46NkPxL7@paws-sandbox-gdqa2.mongodb.net/paws-sandbox?ssl=true&ssl_cert_reqs=CERT_NONE'


# Initialize app instance
# Central registry to view funcs, URL rules
# and template configs
app = Flask(__name__)


app.config['MONGODB_HOST'] = MONGO_URI
app.debug = True

# Initialise app with database
db.init_app(app)


# Routing
@app.route('/')
def index():
    # Get the last date the scraper ran
    for post in Post.objects().fields(date_str=1).order_by('-date_str').limit(1):
        day_to_pull = post.date_str

    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
    )


@app.route("/date")
def all_dates():
    # Get all the dates the scraper was run on
    dates = Post.objects().fields(date_str=1).distinct('date_str')

    return render_template(
        'all_dates.html',
        dates=reversed(list(dates))  # Puts latest date first
    )


@app.route('/date/<day_to_pull>')  # <...> include variable in route
def by_date(day_to_pull=None):
    return render_template(
        'index.html',
        Post=Post,
        day_to_pull=day_to_pull
    )


@app.route('/sub')
def all_subs():
    # Get all the sub that have been scraped
    subs = Post.objects().fields(sub=1).distinct('sub')

    return render_template(
        'all-subreddits.html',
        subs=sorted(list(subs), key=str.lower)
    )


@app.route("/sub/<sub_to_pull>")
def by_subreddit(sub_to_pull=None):
    return render_template(
        'by_subreddit.html',
        Post=Post,
        sub=sub_to_pull
    )


# Execution
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
