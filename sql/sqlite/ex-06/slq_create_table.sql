-- create table product
create table product(
    id integer primary key autoincrement,
    name varchar(255),
    description text,
    price integer
)


-- create table product photo
create table product_photo(
	id integer primary key autoincrement,
	url varchar(255),
	product_id integer,
	foreign key (product_id) references product (id) -- связь через внещний ключ
		on delete cascade
		on update cascade
);

create table client(
	id integer primary key autoincrement,
	name varchar(255),
	phone varchar(30),
	email varchar(255)
);

create table orders(
    id integer primary key autoincrement,
    client_id integer,
    foreign key (client_id) references client (id)
        on delete cascade
        on update cascade
);


create table order_product(
    order_id integer,
    product_id integer,
    foreign key order_id references orders (id)
        on delete cascade
        on update cascade,
    foreign key product_id references product (id)
        on delete cascade
        on update cascade
);

insert into client (name, phone, email) values
('vasia','01','vasia@gamil.com'),
('dima','02','dima@gmail.com')

select * form client





