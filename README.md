# SDS AI Content Driven Project

## Flask server

### Endpoints:

1.  /articles/\<int:num>
    a. GET request, gets the number of articles specified in URL
2.  /delete_article
    a. POST request, expecting a JSON in the form `{'article': 'article_name'}`. Deletes the specified article from the flasks server
3.  /upload_article/\<string:article_title>
    a. POST request, expecting an HTML document as the body (the newly formatted article). Uploads the article and sends notification (still a work in progress).

### Files:

- Server.py contains all the endpoints and the responses sent, but most of the other logic has been outsourced to the functions.py file.
- As mentioned before, functions.py contains a lot of the logic and has some unfinished functions that will be needed in the final product. There are commented out suggestions on how they should work based on the flowchart discussed.
- Article.py contains a class (article_obj) used to store the article objects when they are received. This is really just to enforce a standard form on articles stored on the sever.

### Task scheduling:

Currently being done by apscheduler library, this is the `BackgroundScheduler` found in server.py. Can be configured to run whenever you'd like, just look at their documentation to see how.

### Libraries:

Can all be found in the requirements.txt file.

## To get Google Drive keys and credentials

### Keys:

- go to google cloud console and make a new project
- once that is done, go to IAM & Admin -> service accounts.
- click "create service account"
- assign permissions (I believe I used Editor and Storage Object Admin)
- after creation, click "create key", choose the type as JSON and download it
- rename this to keys.json and put it in this directory

### Credentials:

- in cloud console, go to APIs & services -> library
- search for google drive api and enable it
- after enabling, go to APIs & services -> credentials
- click create credentials and select OAuth client ID
- if it prompts you to set up the consent screen just skip through it, we wont need it
- select the desktop app type and enter a name
- click create and then download json
- rename this to credentials.json and put it in this directory
