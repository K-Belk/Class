Assessment 3 - Database Modeling
--------------------------------

* Due Tuesday at beginning of class
* Do not make a PR until Tuesday at the beginning of class

Backstory
---------
Fast forward 10 weeks. You've finished Code Platoon and you are going to create a ecommerce website for creators to sell their goods directly to consumers. The first thing you need to do? Design a basic schema!

Your client has said that they want to store Customers, Orders, Products, and Categories (e.g., a Pencil `Product` is under the Home Office `Category`. You are not limited to this number of tables, but have to have them at a minimum.

For this assessment, you have your choice of using raw SQL or Python/SQL together. If you want to finish this assessment using raw SQL, please look in the `sql/` folder. If you want to finish this assessment using Python/SQL, please look in the `python/` folder.

`schema.sql` / `schema_creation.py`
------------
- Create the tables and appropriate relationships for the tables above.
  - Customers have first and last names, dates of birth, addresses, and email addresses
  - Categories have names
  - Products have names and prices
  - An order must be able to contain multiple products

**Hints**
  - Consider the order of tables when you create them
  - Remember to have drop table statements if you're running things over and over again
  - You are going to need join tables

`seeds.sql` / `seeds.py`
-----------
- Create & insert at least 3 records for each table.

`queries.sql` / `queries.py`
-------------
- Retrieve the customers with a Gmail email address
- Retrieve the customers under 25 years old
- Retrieve customer ID 2's orders
- Retrieve customer ID 2's purchased products
- Retrieve all the products under a the "Home Office" category
- Retrieve all the orders that have a product which belongs to the "Kitchen" category
