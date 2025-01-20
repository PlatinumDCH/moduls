--переименовать колонкуА в колонкуБ и датть ей тип integer
alter table table_name change column_a column_b integer

--поменять только тип колонки 
alter table table_name modify column_b bigint not null

--подабвить новую колонку --удалить ее уже нельзя только пересоздавать таблицу
alter table table_name add column float

--добавить новую колонку с указанныи типом после указанной колонки
alter table table_name add column_a varhcar(30) after column_b

--добавть колонку с указанным типов и сделать ее первой нелзя оформить в sqlite 
alter table table_name add collumn char(10) first

--удалить колонку в таблице
alter table table_name drop Column column_name

alter table table_name add index index_name_ix (column_name)



