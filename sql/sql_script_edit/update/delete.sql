delete from contacts where id = 4


-- удаление всех данных из таблицы но оставить название колонок
delete from <nameTable>

-- удаление щетчика автоинкремена
DELETE FROM sqlite_sequence WHERE name='name_table';
UPDATE sqlite_sequence SET seq = <n> WHERE name = '<table>';

-- удаление всей таблицы
drop table contacts

--postgresql обнуление щетчика
SELECT pg_get_serial_sequence('table', 'id'); -> <nameRow>
ALTER SEQUENCE name_row RESTART WITH 1;
