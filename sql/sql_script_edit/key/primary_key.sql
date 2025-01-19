create table users(
    name char(10) not null,
    surname char(10) not null,
    avtobiograpfy text not null
)

alter table users add constraint table_id_pk primary key(id);

alter table users drop primary key;

