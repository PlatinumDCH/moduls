select id from users where age < 30

select *
from contacts
where user_id in (select id from users where age < 30)