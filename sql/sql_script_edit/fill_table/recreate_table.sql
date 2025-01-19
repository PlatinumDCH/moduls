
--создано новую таблицу
create table new_table (
    id integer primary key,
    surname char(10),
    name text
);

insert into test_new(id, name)
select id, name from test;

drop table test;  -- удалить  старую таблицу 
alter table test_new rename to test; --переименовать
