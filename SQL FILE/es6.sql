-- almeno una citta
select c.Name as NAzioni
from country as c
where exists
(select 1 from city as ci where ci.CountryCode = c.Code);

-- linguue nazioni A
select distinct cl.Language
from country as c
-- join countrylanguage cl on c.Code = cl.CountryCode
join countrylanguage cl on c.Code in 
(select c.Code 
where c.Name like 'A%');
