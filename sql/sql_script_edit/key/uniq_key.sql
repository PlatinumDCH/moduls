create table persons (
    id int primary key,
    email char(50) not null,
    fullname varchar(100) null,
    constraint persons_email_un unique key (email)
);

alter table persons add constraint persons_email_un unique key (email);

