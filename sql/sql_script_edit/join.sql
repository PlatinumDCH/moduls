select users.id, users.name, users.email, g.name AS genger
from users 
inner join genders as g on g.id = u.gender_id


select contacts.id, contacts.name, contacts.email, users.name 
from contacts
join useres on useres.id = contacts.user_id
