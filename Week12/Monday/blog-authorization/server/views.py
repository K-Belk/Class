import sqlite3
import json
import base64
import hashlib
import json
from login import handle_options, login_required


def build_json_response(json_body, code="200 OK"):
    # "Access-Control-Allow-Headers:*" is to handle a CORS issue in the browser
    return f"HTTP/1.1 {code}\r\nContent-Type:application/json\r\nAccess-Control-Allow-Origin:*\r\nAccess-Control-Allow-Headers:*\r\nContent-Length:{len(json_body)}\r\n\r\n{json_body}"


# @login_required  # You will need to implement this decorator
def handle_posts(request):
    if request["method"] == "GET":
        with sqlite3.connect("../database/blog_db.sqlite") as conn:
            all_posts_query = """
            select title,contents,username from Post join User on Post.user_id = User.id;
            """
            cur = conn.cursor()
            all_posts = cur.execute(all_posts_query).fetchall()
            all_posts_formatted = [{"author": p[2], "title": p[0], "content": p[1]} for p in all_posts]
        conn.close()
        return json.dumps({"data": all_posts_formatted})
    elif request["method"] == "POST":
        return json.dumps({"req": "posts POST"})


def handle_login(request):
    if request["method"] == "OPTIONS": return handle_options() # to handle CORS issue in browser
    if request["method"] == "GET":
        # Your code here
        return json.dumps({"req": "login GET"})
    elif request["method"] == "POST":
        # Your code here
        return json.dumps({"req": "login POST"})