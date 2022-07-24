import sqlite3
import random
import string
import json


def handle_options():
    return json.dumps({"options": "don't worry about it"})


def login_required(f):
    def inner(request):
        if request["method"] == "OPTIONS": return handle_options() # to handle CORS issue in browser
        # Your code here
    return inner