-- не нужно указывать id, он сам будет записыватся

create table users(
    id integer primary key autoincrement,
    username text not null default 'exemple_username'
);

insert into users (username) values ('alice');
insert into users (username) values ('dima');

select * form users;

