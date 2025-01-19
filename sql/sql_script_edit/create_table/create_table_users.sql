create table users(
	id int primary key, --уникальный ключ
	name varchar(30), --имя пользователя
	email varchar(30), --почта пользователя
	password varchar(30), --пароль пользователя
	age TINYINT unsigned, --возраст пользователя
	gender_id int, -- связь таблицы users и genders
	created_at timestamp default current_timestamp, --когда был создан
foreign key (gender_id) references genders(id)
	on delete set NULL --если удал знач genders установить значение в users = Null
	on UPDATE cascade --если будет изменено значение в genders то это изменение будет и users
);

