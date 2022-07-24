import sqlite3
import json


def clear_tables():
    with sqlite3.connect("blog_db.sqlite") as conn:
        drop_tables = """
        drop table if exists User;
        drop table if exists Post;
        """
        cur = conn.cursor()
        cur.executescript(drop_tables)
    conn.close()

def create_tables():
    with sqlite3.connect("blog_db.sqlite") as conn:
        create_users_table = """
        create table User (
            id integer primary key,
            username text,
            email text,
            password text,
            token text
        );
        """
        create_posts_table = """
        create table Post (
            id integer primary key,
            title text,
            contents text,
            user_id integer,
            foreign key(user_id) references User(id)
        );
        """
        cur = conn.cursor()
        cur.execute(create_users_table)
        cur.execute(create_posts_table)
    conn.close()

def insert_users(username, email, password):
    base = f"insert into User(username, email, password) values('{username}', '{email}', '{password}');"
    return base

def insert_posts(title, contents, user_id):
    base = f"insert into Post(title, contents, user_id) values('{title}', '{contents}', '{user_id}');"
    return base

def populate_initial_data():
    with open('initial_data.json', 'r') as f:
        js = json.load(f)
        js_users = js["users"]
        js_posts = js["posts"]

        all_users = " ".join([insert_users(u["username"], u["email"], u["password"]) for u in js_users])
        all_posts = " ".join([insert_posts(p["title"], p["contents"], p["user_id"]) for p in js_posts])

        with sqlite3.connect("blog_db.sqlite") as conn:
            cur = conn.cursor()
            cur.executescript(all_users)
            cur.executescript(all_posts)
        conn.close()


if __name__ == "__main__":
    print("initializing database...")
    clear_tables()
    create_tables()
    populate_initial_data()
    print("database initialized...")

