create table genders(
    id int primary key, -- уникальный ключ обьектов таблицы
    name varchar(30), -- название гендера 
    created_at timestamp default CURRENT_TIMESTAMP -- когда был создан
);
