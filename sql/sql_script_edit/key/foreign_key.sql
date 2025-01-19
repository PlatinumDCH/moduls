create table genders (
    id int primary key,
    name varchar(30),
    created_at timestamp default current_timestamp
);

create table users (
    id int primary key,
    name varchar(30),
    email varchar(30),
    password varchar(30),
    age tynint unsigned,
    gender_id int,
    created_at timestamp default current_timestamp,
    foreign key (gender_id) references genders (id)
        on delete set null
        on update cascade
        
)