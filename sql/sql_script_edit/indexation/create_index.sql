create index name_index on table_name (nameCollumn)

create table table1
(
    id integer unsigned autoincrement,
    code char(4) not null default 'ffff',
    name varchar(50) not null default '' ,
    description text not null default '', comment 'description prod',
    price float not null default 0 comment 'price product',
    index table1_name_ix(name),
    index table1_price_ix(price)
) comment 'table ptoducts fith key and index'


alter table table1 add index table1_name_ix(name), add index table1_price_ix(price);

create index teble_name_ix on table_1 (name);
create index table_1_name_price_ix on table_1 (name, price);

---drop index
drop index table_price_ix on table1;

