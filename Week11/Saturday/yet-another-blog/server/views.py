import sqlite3
import json
import sys

sys.path.append('/Users/kevinlbelk/Documents/Programing/CodePlatoon/Week11/Saturday/yet-another-blog/')
from database.initialize_db import insert_users, insert_posts

def build_json_response(json_body):
    return f"HTTP/1.1 200 OK\r\nContent-Type:application/json\r\nContent-Length:{len(json_body)}\r\n\r\n{json_body}"

def handle_users(request):
    if request["method"] == "GET":
        return json.dumps({"req": "users GET"})
    elif request["method"] == "POST":
        return json.dumps({"req": "users POST"})

def get_user_id(username):
        with sqlite3.connect("../database/blog_db.sqlite") as conn:
            user_query = """
            SELECT username, id from User;
            """
            cur = conn.cursor()
            users = cur.execute(user_query).fetchall()
        conn.close()
        user_list = [ name for name in users if name[0] == username]
        if len(user_list) > 0:
            return user_list[0][1]
        else :
            with sqlite3.connect("../database/blog_db.sqlite") as conn:
                cur = conn.cursor()
                cur.executescript(insert_users(username, f'{username}.gmail.com'))
            conn.close()
            return ((users[-1][1]) + 1)

def all_post():
    with sqlite3.connect("../database/blog_db.sqlite") as conn:
        all_posts_query = """
        select title,contents,username from Post join User on Post.user_id = User.id;
        """
        cur = conn.cursor()
        all_posts = cur.execute(all_posts_query).fetchall()
        all_posts_formatted = [{"author": p[2], "title": p[0], "content": p[1]} for p in all_posts]
    conn.close()
    return all_posts_formatted
    

def handle_posts(request):
    if request["method"] == "GET":
        all_posts_formatted =  all_post()
        return json.dumps({"data": all_posts_formatted})
    elif request["method"] == "POST":
        user_id = get_user_id(request['author'])
        with sqlite3.connect("../database/blog_db.sqlite") as conn:
            cur = conn.cursor()
            cur.executescript(insert_posts(request['title'], request['content'], user_id ))
        conn.close()
        all_posts_formatted =  all_post()
        return json.dumps({"data": all_posts_formatted})

