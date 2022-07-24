
INSERT INTO menu_items (id, dish) VALUES(1, 'Classic Booger Burger');

INSERT INTO addresses (id, street, street2, city, state, zip_code) VALUES (1, '123 seaseme street', '' , 'New York', 'New York', '12345');
INSERT INTO addresses (id, street, street2, city, state, zip_code) VALUES (2, '638 E University Blvd', '' , 'New York', 'New York', '85705');

INSERT INTO restaurants (id, name, address_id, menu_item_id) VALUES (1, 'Boogers Burgers', 2, 1 );

INSERT INTO orders (id, restaurant_id) (VALUES (1, 1));

INSERT INTO users (id, user_name, address_id, order_id) VALUES(1, 'kevin', 1, 1);

