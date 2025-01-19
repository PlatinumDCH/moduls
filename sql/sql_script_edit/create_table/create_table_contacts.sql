create table contacts (
	id int primary key, --порядковый номер кнотакта, уникальный ключ
	name varchar(30), --название котакта
	email varchar(30), --почта контакта
	phone varchar(30), --телефон контакта
	favorite boolean, --контакт находится в избранном
	user_id int, --связь таблицы пользователь и контакт

	created_at timestamp default current_timestamp, --когда был создан
	foreign key (user_id) references users (id)
		on delete cascade --если удалить пользователя удалится и контакт
		on update cascade --если идентификатор пользователя обновить то обновится и в этой таблице
);

