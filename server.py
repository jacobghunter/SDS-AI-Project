from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, Response, jsonify, request, render_template
import functions
from article import article_obj


app = Flask(__name__)

# this route is for testing, delete from production
@app.route("/article", methods=['GET'])
def get_article():
    # functions.get_article("Hello, World!")
    a = article_obj("Hello, World!", "This is a test article.")
    # functions.store_articles([article_obj("wazzup, World!", "This is a test article."), article_obj("Helo, World!", "This is a test article.")])
    # functions.remove_article("Hello, World!")
    functions.upload_article("test")
    return a.toDict()

# for getting a specified number of articles
@app.route("/articles/<int:num>", methods=['GET'])
def articles(num):
    try:
        return functions.get_articles(num)
    except:
        return Response(status=500)

# for deleting an article
@app.route("/delete_article", methods=['POST'])
def delete_article():
    if request.method == 'POST':
        try:
            article = request.json['article']
        except:
            return Response(status=400, response="Expecting the form {'article': 'article_name'}")
        if functions.remove_article(article):
            return Response(status=200)
        else:
            return Response(status=404, response="Article not found")

# for uploading an article to docs/wordpress once approved
@app.route("/upload_article/<string:article_title>", methods=['POST'])
def upload_article(article_title):
   if request.method == 'POST':
        try:
            # reading HTML sent from frontend and storing it tempororily
            with open(f'{article_title}.html', 'w+') as f:
                f.write(request.data.decode('utf-8'))
        except:
            return Response(status=400, response="Expecting an HTML document in the body of the request.")
        try:
            # make sure your keys and credentials for google drive have been added to the drive_upload.py file
            functions.upload_article(article_title)
            return Response(status=200)
        except:
            return Response(status=500)
        
# scheduler for loading articles once a day 
scheduler = BackgroundScheduler(timezone="America/Los_Angeles")
# Runs from Monday to Friday at 5:30 (am)
scheduler.add_job(
    func=functions.load_articles,
    trigger="cron",
    max_instances=1,
    day_of_week='mon-fri',
    hour=5,
    minute=30
)
scheduler.start()

if __name__ == "__main__":
  app.run(debug=True, port=8000)