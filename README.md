# SDS AI Content Driven Project

## Running on the ubuntu server

### First time setup (already done on the system with ip: 167.99.111.147)

1. Install Python 3.11.8 on the system (should not have an issue upgrading, this is just what was used to develop)
2. Go to the directory you want this installed in and clone this repo
3. Make a python [virtual environment](https://docs.python.org/3/library/venv.html)
4. Enter the virtual environment using `source venv/bin/activate` (using `deactivate` will go back to the global python install)
5. Install the required packages using `pip install -r requirements.txt`
6. Install [Caddy](https://caddyserver.com/docs/install#debian-ubuntu-raspbian) for the reverse proxy (this will start automatically on install, you can stop it with `caddy stop`)

### Running the Flask server

1. cd into the directory this project is in.
2. Run the command: `source venv/bin/activate`
3. Start Caddy using `sudo caddy start`
4. Starting the server:
   1. To start the server in production mode, run `gunicorn server:app` or `gunicorn server:app --daemon` to run it in the background
   2. To start the server in development mode, run `python3 server.py`
5. Once all this is done, you can visit `http://167.99.111.147/article` via a web browser and see the expected JSON response or make requests to `http://167.99.111.147` based on the endpoints listed below.

### Shutting down Flask server

1. To stop caddy, run `caddy stop`. If multiple are running, this will need to be run until you see an error code to make sure another instance isnt going in the background
2. To stop gunicorn, if it was run using the non-daemon version, just do `crtl-c`. If it was run Using daemon, you can run `pkill -f gunicorn` or find it using `top` and kill it by its id

## Flask server details

### Endpoints:

1.  /articles/\<int:num>
    1. GET request, gets the number of articles specified in URL
2.  /delete_article
    1. POST request, expecting a JSON in the form `{'article': 'article_name'}`. Deletes the specified article from the flasks server
3.  /upload_article/\<string:article_title>
    1. POST request, expecting an HTML document as the body (the newly formatted article). Uploads the article and sends notification (still a work in progress).

### Files:

- Server.py contains all the endpoints and the responses sent, but most of the other logic has been outsourced to the functions.py file.
- As mentioned before, functions.py contains a lot of the logic and has some unfinished functions that will be needed in the final product. There are commented out suggestions on how they should work based on the flowchart discussed.
- Article.py contains a class (article_obj) used to store the article objects when they are received. This is really just to enforce a standard form on articles stored on the sever.

### Task scheduling:

Currently being done by apscheduler library, this is the `BackgroundScheduler` found in server.py. Can be configured to run whenever you'd like, just look at their documentation to see how.

### Libraries:

Can all be found in the requirements.txt file.

## To get Google Drive keys and credentials (currently not working and commented out in the code)

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
