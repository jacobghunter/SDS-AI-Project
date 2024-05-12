import json
from article import article_obj
import aspose.words as aw
import os
import drive_upload

def get_article(title: str):
    # with open('articles.json', 'w') as f:
    #     articles = json.load(f)
    #     try:
    #         articles[title]
    return article_obj("Hello, World!", "This is a test article.").toDict()

def load_articles():
    # articles = get_potential_articles() # returns a list of articles
    # summarizations = summarize_articles(articles) # returns summarizations of articles in dict
    # store_articles(summarizations) # stores summarizations in a json or database if needed
    return True

def store_articles(articles: list[article_obj]):
    with open('articles.json', 'r+') as f:
        try:
            # load previous articles if they exist
            json_articles = json.load(f)
        except:
            # if none exist, create a new dict
            json_articles = {}
        
        # add new articles to the dict
        for article in articles:
            json_articles.update(article.toJSON())
            
        json_obj = json.dumps(json_articles)

        # overwrite previous file
        f.seek(0)
        f.write(json_obj)
        f.truncate()
    
def remove_article(article_name : str):
    with open('articles.json', 'r+') as f:
        try:
            articles = json.load(f)
            try:
                del articles[article_name]
                json_obj = json.dumps(articles)

                f.seek(0)
                f.write(json_obj)
                f.truncate()
                return True
            except:
                raise Exception("Article not found")
        except:
            raise Exception("No articles found")
        
def get_articles(num):
    with open('articles.json', 'r') as f:
        json_articles = json.load(f)
        articles = []
        i = 0
        for title, content in json_articles.items():
            if i == num:
                break
            articles.append({"title": title, "content": content})
            i+=1
        return articles[:num]
        
def upload_article(article_name: str):
    try:
        upload_article_docs(article_name) # not working yet, need to get the upload to show up in the user's drive
        
        # upload_article_wordpress(article_name)
        
        # os.remove(f"{article_name}.html") # delete temp HTML file
        # remove_article(article_name) # remove article from local json storage
        # send_email() # send email to jeevan with uploaded article
        return True
    except:
        raise Exception("Error uploading article")
        
def upload_article_wordpress(article_name: str):
    # upload to wordpress
    return

def upload_article_docs(article_name: str):
    aw.Document(f"{article_name}.html").save(f"{article_name}.doc") # convert to docx for file upload
    
    # upload to google docs
    drive_upload.get_file()
    # drive_upload.upload_document(f'{article_name}.doc', f'{article_name}.doc')

    os.remove(f"{article_name}.doc") # remove the docx file after upload
    return

def convert_articles(articles: dict):
    return_articles = []
    for article in articles:
        return_articles.append(article_obj.fromDict(article))
    return return_articles

def send_email():
    # send email to jeevan
    return