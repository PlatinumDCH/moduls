create table contacts(
    id integer primary key autoincrement,
    name char(15) not null,
    fullname char(15) not null,
    phone varchar(30) not null,
)

insert into contacts (name, fullname, phone) values 
('dima', 'dima cheban', '0672730962'),
('test', 'test testing', '0671212312')


--указание алиасов для колонок name fullname
select name as naming, fullname as fullName from contacts
--указание аласов для колонок name fullname без as 
select name naming, fullname fullNeme from contacts



crate table jj(
    id integer primary key autoincrement,
    material varchar(50),
    number_production int,
    create_at timestamp default current_timestamp
)

insert into jj (material, number_production) values
('material_1', 00000),
('material_2', 11111),
('material_3', 22222),
('material_4', 33333)

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_prod VARCHAR(30) NOT NULL,
    price INT NOT NULL,
    jj_id INT NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (jj_id) REFERENCES jj(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

insert into products (   name_prod,  price, jj_id) values
                        ('productA', 100,    1),
                        ('productB', 200,    2),
                        ('productC', 300,    3),
                        ('productD', 400,    4)

--with alias
select pr.name_prod, pr.price j.material
from products as pr
join jj as j on pr.jj_id = j.id

--wothout alias
select products.name, products.price, jj.material
from products
join jj on products.jj_id = jj.id

--modern alias
-- алиасы с пробелами или дефисами нужно заключать в кавычки
select name_prod as "Products Name", price as "Products Price"
from products

--использование алиасов для вычисления значений
select price, price * 0.9 as discount_price
from products

