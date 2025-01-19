select min(age) as minAge from users --найти миимальный возравст среди пользователей

select avg(age) as averageAge from users -- найт средний возраст пользователей

select  count(user_id) as total_contacs, user_id
from contacts
group by user_id


