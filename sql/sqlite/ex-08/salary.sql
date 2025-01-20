-- table: companies
drop table if exists companies;
create table companies (
    id integer primary key autoincrement,
    company_name varchar(255) unique not null
);

--table: employees
drop table if exists employees;
create table employees (
    id integer primary key autoincrement,
    employees varchar(255) unique not null,
    post varchar(120) not null,
    company_id integer,
    foreign key (company_id) references companies (id)
        on delete cascade
        on update cascade
);

--table: payments
drop table if exists payments;
create table payments (
    id integer primary key autoincrement,
    employee_id integer,
    date_of text not null,
    total text not null, -- Используем TEXT для ISO8601
    foreign key (employee_id) references employees (id)
        on delete cascade
        on update cascade
);

