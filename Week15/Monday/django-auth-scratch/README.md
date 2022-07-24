# Django Authentication

## Requirements
Create a project and two apps.  The first app can be whatever you like, but the second app should be called `authenticate`.  `authenticate` will handle the following routes:

- signup/
- login/
- logout/

`authenticate` should contain your main user model.  You can either use the User/Profile one-to-one pattern, or customize the User model (or if you are really crazy just a plain old model).  

You should have at least two routes for your second app.  At least one of them should be protected.

Be sure to write tests.