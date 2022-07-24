drop table if exists account cascade;
drop table if exists seller_account cascade;
drop table if exists car_model cascade;
drop table if exists car cascade;
drop table if exists advertisement cascade;


CREATE TABLE account (
	account_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	CHECK(first_name !~ '\s' AND last_name !~ '\s'),
	CHECK (email ~* '^\w+@\w+[.]\w+$'),
	CHECK (char_length(password)>=8)
);


CREATE TABLE seller_account (
	seller_account_id SERIAL PRIMARY KEY,
	account_id INT NOT NULL REFERENCES account(account_id),
	street_name TEXT NOT NULL,
	street_number TEXT NOT NULL,
	zip_code TEXT NOT NULL,
	city TEXT NOT NULL
);


CREATE TABLE car_model
(
	car_model_id SERIAL PRIMARY KEY,
	make text,
	model text,
	UNIQUE (make, model)
);


CREATE TABLE car (
	car_id SERIAL PRIMARY KEY,
	number_of_owners INT NOT NULL,
	registration_number TEXT UNIQUE NOT NULL,
	manufacture_year INT NOT NULL,
	number_of_doors INT DEFAULT 5 NOT NULL,
	car_model_id INT NOT NULL REFERENCES car_model (car_model_id),
	mileage INT
);


CREATE TABLE advertisement(
	advertisement_id SERIAL PRIMARY KEY,
	advertisement_date TIMESTAMP WITH TIME ZONE NOT  NULL,
	car_id INT NOT NULL REFERENCES car(car_id),
	seller_account_id INT NOT NULL REFERENCES seller_account (seller_account_id)
);
