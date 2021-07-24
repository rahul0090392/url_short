# url_short
An API service to shorten URL


RUNNING LOCALLY:-

CLONE REPOSITORY
STEPS:-
1. create python virtual environment
    virtualenv venv -p python3
2. Install Requirements
    pip install -r requirements.txt
3. Runserver
    python manage.py runserver

By default server runs on 8000 port

API Details

URL:- http://localhost:8000/api/manageurl/shorten_url
METHOD:- POST
BODY: - {
    "url":"your_url"
}

RESPONSE:

{
    "status": "success",
    "shorten_url": "https://shorten.com/AAA="
}

RESPONSE ERROR:

{
    "status": "error",
    "details": {
        "url": [
            "This field may not be blank."
        ]
    }
}
