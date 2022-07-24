(# Posts and Comments
You are going to create an app where you can view posts and the comments associated with that post. This is going to be very similar to the polls/votes tutorial found in the first day of Django curriculum. Since it's your first day of Django, we want you to build everything from scratch to get a better grasp of the material. 

## Release 0
Set up your Django project and app. Ensure that they are registered with each other.

## Release 1
Create your routes in `urls.py`. Ultimately, we want to get to this app having 2 routes:
- `/posts`: All posts
- `/posts/:id`: Information about a post with that specific ID number. If a post has corresponding comments, we want to see that on this page as well.

## Release 2
Set up your database with your two associated models and migrate them into your database. Specifically, I want a `Post` to have a `title` and `body`. A `Comment` should have a `body` and belong to a `Post`

## Release 3
Populate the database using the Django shell. Create 3 posts with 2 comments associated with them.

## Release 4
Create your HTML views using helper methods
