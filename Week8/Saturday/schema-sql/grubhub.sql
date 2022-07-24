DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS restaurants CASCADE;
DROP TABLE IF EXISTS menu_items CASCADE;
DROP TABLE IF EXISTS addresses CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE menu_items (
    id  SERIAL PRIMARY KEY,
    dish varchar(255)   NOT NULL
);

CREATE TABLE addresses (
    id  SERIAL PRIMARY KEY,
    street varchar(255)   NOT NULL,
    street2 varchar(255),
    city varchar(255)   NOT NULL,
    state varchar(255)   NOT NULL,
    zip_code varchar(255)   NOT NULL
);

CREATE TABLE restaurants (
    id  SERIAL PRIMARY KEY,
    name varchar(255)  NOT NULL,
    address_id int   NOT NULL,
    menu_item_id int   NOT NULL,
    FOREIGN KEY(address_id) REFERENCES addresses(id),
    FOREIGN KEY(menu_item_id) REFERENCES menu_items(id)
);

CREATE TABLE orders (
    id  SERIAL PRIMARY KEY,
    restaurant_id int   NOT NULL,
    FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
);

CREATE TABLE users (
    id  SERIAL  PRIMARY KEY,
    user_name varchar(255)   NOT NULL,
    address_id int   NOT NULL,
    order_id int   NOT NULL,
    FOREIGN KEY(address_id) REFERENCES addresses(id),
    FOREIGN KEY(order_id) REFERENCES orders(id)
);


