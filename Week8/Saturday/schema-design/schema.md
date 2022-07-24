#Visualize your schema

Open this file in your text editor and visualize your schema. At the top is your table name. Listed below are all the columns in that table. 

User
-------------------
id
first_name
last_name

Address
-------------------
id
user_id
street 
street2 
city
state
zip_code
country

In the example above, each Address can belong to a User. This is achieved by adding a column called `user_id`, which can match only ONE of the values in the `id` column of the User table. Remember, `id`s are unique; no table can have two `id` values that are the same.

Using the above format, jot down the database for your apps below!

## GrubHub Online Ordering
orders
------------
id AUTOINCREMENT PK int IDENTITY
restaurant_id int FK >- restaurants.id
user_id int FK - users.id

restaurants
------------
id AUTOINCREMENT PK int IDENTITY
name varchar(255),
address_id int FK -< addresses.id
menu_item_id int FK >- menu_items.id

menu_items
------------
id AUTOINCREMENT PK int IDENTITY 
dish varcahr(255)

users
------------
id AUTOINCREMENT PK int IDENTITY
user_name varchar(255)
address_id int FK >- addresses.id
order_id int FK >- orders.id

addresses
------------
id AUTOINCREMENT PK int IDENTITY
street varchar(255),
street2 varchar(255),
city varchar(255),
state varchar(255),
zip_code varchar(255)

## Blue Apron

Users
------------
id AUTOINCREMENT PK int IDENTITY
last_name varchar(100)
first_name varchar(100)
address varchar(100)
service_plan_id int FK - Service_Plans.id
delivery_id FK -< Deliveries.id

Service_Plans
------------
id AUTOINCREMENT PK int IDENTITY
promotion_id FK - Promotions.id
meal_number int
frequency int

Recipes
------------
id AUTOINCREMENT PK int IDENTITY
wellness_id FK -< Wellness_Recipes.id
vegetarian_id FK -< Vegetarian_Recipes.id
signature_id FK -< Signature_Recipes.id

Signature_Recipes
------------
id AUTOINCREMENT PK int IDENTITY
recipe varchar(100)

Vegetarian_Recipes
------------
id AUTOINCREMENT PK int IDENTITY
recipe varchar(100)

Wellness_Recipes
------------
id AUTOINCREMENT PK int IDENTITY
recipe varchar(100)

Promotions
------------
id AUTOINCREMENT PK int IDENTITY
discount int

Deliveries
------------
id AUTOINCREMENT PK int IDENTITY
recipe_id FK -< Recipes.id


## Instagram

users
------------
id AUTOINCREMENT PK int IDENTITY
post_id int FK -< posts.id
follow_id  int FK -< follows.id
following_id int  FK - followings.id

posts
------------
id AUTOINCREMENT PK int IDENTITY 
photo_id int FK -< photos.id
comments_id int FK -< comments.id
likes_id int FK -< likes.id

photos
------------
id AUTOINCREMENT PK int IDENTITY
post varchar(255)

comments
------------
id AUTOINCREMENT PK int IDENTITY
commenter_user_id int FK - users.id
comment varchar(255)

likes
------------
id AUTOINCREMENT PK int IDENTITY
liker_user_id int FK - users.id

follows
------------
id AUTOINCREMENT PK int IDENTITY
user_id int FK - users.id

followings
------------
id AUTOINCREMENT PK int IDENTITY
user_id int FK - users.id