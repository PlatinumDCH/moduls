select name, email
from contacts
where favorite = true --выбираем только те строки в которых favorite = true
order by name


select name, email
from users
where age in(20, 30, 40)
order by name

select name, email, age
from users
where age between 30 and 40
order by name

select name, email
from contacts
where name like '%L%'
order by name

select name, email, age
from users
where age not between 30 and 40
order by name

