# Wow, Another Blog Site!

## Requirements
You, an up-and-coming team of fullstack engineers, have been tasked with creating the front end (and improving the back end) of yet another blog site.  There is already a backend API, but its functionality is very limited, and the code is not the prettiest.  

It returns JSON, as you might expect.  

There are only two routes that you need to worry about: `/posts` and `/users`.  Right now, if you make a GET request to `/posts`, you will get all the posts in the database.  It sure would be nice to see those on a webpage.

The acute observer will have noticed some starter code for handling a POST request to `/posts`.  Visitors to your site should be able to add new blog posts (don't worry about authentication, they can just include the author's username in the form).  In adhering to standard practice, visitors should be redirected to `/posts` (with a GET) after adding a new post to see their new post included with the others.

After you get that working, your application should also be able to handle signing up new users.

## Instructions to Get Started
`cd` into the `database` folder and run `initialize_db.py`.  That will create and populate your application's database.  Once you have the database, you can `cd` into `server` and run `server.py`. When your database and server are up, you can start working.

## Tools
- If you want to make things a little easier for yourself, you can use this sqlite [GUI](https://sqlitebrowser.org/)
- Don't forget about Postman

## Personal Growth
During this project, you might find that you are experiencing some of the following opportunities to become a better you:
- post vs. POST.  One day you'll learn to laugh about it.
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) error: Read the error message in your browser.  It basically tells you what you need to do.  Remember that you have full control over the headers you send.  It almost feels like cheating.