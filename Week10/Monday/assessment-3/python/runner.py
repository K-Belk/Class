from queries import Queries
from schema import Schema
from seeds import Seed




Schema().main("categories", "id SERIAL PRIMARY KEY , name TEXT NOT NULL")
Schema().main("addresses", "id SERIAL PRIMARY KEY , street1 TEXT NOT NULL, street2 TEXT, city TEXT NOT NULL, state TEXT NOT NULL, zip_code TEXT NOT NULL")
Schema().main("products", "id SERIAL PRIMARY KEY , name TEXT NOT NULL, price decimal NOT NULL, category_id INT NOT NULL REFERENCES categories(id)")
Schema().main("customers", "id SERIAL PRIMARY KEY , first_name TEXT NOT NULL, last_name TEXT NOT NULL, dob DATE NOT NULL, address_id INT NOT NULL REFERENCES addresses(id), email_address TEXT NOT NULL")
Schema().main("orders", "id SERIAL PRIMARY KEY, customer_id INT NOT NULL REFERENCES customers(id)")
Schema().main("orders_products", "id SERIAL PRIMARY KEY , order_id INT NOT NULL REFERENCES orders(id), product_id INT NOT NULL REFERENCES products(id)")

Seed().main("categories", "name", ("Printers",))
Seed().main("products", "name, price, category_id", ("CR-10", 400.00, 1))
Seed().main("products", "name, price, category_id", ("Ender3", 350.00, 1))
Seed().main("products", "name, price, category_id", ("Pursa i3", 900.00, 1))

Seed().main("categories", 'name', ("Filament",))
Seed().main("products", "name, price, category_id", ("PLA", 22.00, 2))
Seed().main("products", "name, price, category_id", ("PETG", 26.00, 2))
Seed().main("products", "name, price, category_id", ("ABS", 31.00, 2))

Seed().main("categories", 'name', ("Parts",))
Seed().main("products", "name, price, category_id", ("Hot end", 57.00, 3))
Seed().main("products", "name, price, category_id", ("Nozzle", 6.00, 3))
Seed().main("products", "name, price, category_id", ("Nozzle Heater", 15.00, 3))

Seed().main('addresses', 'street1, city, state, zip_code', ("123 ABC Street", "Salem", "Massachuset", "12345"))
Seed().main('customers', "first_name, last_name, dob, address_id, email_address", ("Kevin", "Belk", '1940-02-29', 1, "kevin@gmail.com"))
Seed().main('orders', "customer_id", (1,))
Seed().main('orders_products', "order_id, product_id", (1, 3))
Seed().main('orders_products', "order_id, product_id", (1, 4))
Seed().main('orders_products', "order_id, product_id", (1, 5))

Seed().main('addresses', 'street1, city, state, zip_code', ("987 ZYX Street", "New York", "New York", "54321"))
Seed().main('customers', "first_name, last_name, dob, address_id, email_address", ("Zella", "Belk", '2000-02-29', 2, "zella@yahoo.com"))
Seed().main('orders', "customer_id", (2,))
Seed().main('orders_products', "order_id, product_id", (2, 1))
Seed().main('orders_products', "order_id, product_id", (2, 4))

Seed().main('addresses', 'street1, city, state, zip_code', ("567 IJK Street", "Seatale", "Washington", "67890"))
Seed().main('customers', "first_name, last_name, dob, address_id, email_address", ("Dave", "Mustang", '1970-02-28', 3, 'dave@aol.com'))
Seed().main('orders', "customer_id", (3,))
Seed().main('orders_products', "order_id, product_id", (3, 2))
Seed().main('orders_products', "order_id, product_id", (3, 5))

Seed().main('orders', "customer_id", (1,))
Seed().main('orders_products', "order_id, product_id", (4, 7))

while True:
    print(f"""

1 --Retrieve the customers with a Gmail email address
2 --Retrieve the customers under 25 years old
3 --Retrieve customer ID 2's orders
4 --Retrieve customer ID 2's purchased products
5 --Retrieve all the products under a the "Filament" category
6 --Retrieve all the orders that have a product which belongs to the "Printers" category
7 --Quit

    """)
    x = input("Select your query\n")
    if x == "1":
        print('\n')
        Queries().main("select * from customers where email_address like '%gmail%'")
    elif x == "2":
        print('\n')
        Queries().main("select * from customers where extract(year from age(dob))<25")
    elif x == "3":
        print('\n')
        Queries().main("select id from orders where customer_id = 2")
    elif x == "4":
        print('\n')
        Queries().main("select customer_id, order_id, product_id, name, price from orders inner join orders_products on orders.id = order_id inner join products on product_id = products.id where customer_id = 2")
    elif x == "5":
        print('\n')
        Queries().main("select * from products where category_id = 2")
    elif x == "6":
        print('\n')
        Queries().main("select order_id from categories inner join products on categories.id = category_id inner join orders_products on products.id = product_id where categories.id = 1")
    elif x == "7":
        break
