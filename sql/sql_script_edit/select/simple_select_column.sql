select name, email, from contacts order by name
-- order by name asc, сортировка по увеличению за колонкой name(default)
-- order by email desc, сортировка по уменьшению за колонкой email

-- сортировка влияет только на порядок строк, порядок вывода колонок остается неизменные


select colum_1, id, colum_2, name, country_code, app --интересующие поля
from priduct.users --название таблицы
order by age desc, country_code