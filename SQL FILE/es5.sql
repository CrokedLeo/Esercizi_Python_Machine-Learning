-- lingue x nazione x percent
select
c.Name as Nazione,
cl.Language,
cl.Percentage
from country c 
join countrylanguage cl on c.Code = cl.CountryCode
where exists
(select 1 from countrylanguage sub
where sub.CountryCode = cl.CountryCode)
order by c.Name, cl.Percentage desc;


-- nazione x percent lingua 

select 
c.Name as Nazione,
cl.Language,
cl.Percentage
from country c
join countrylanguage cl on c.Code = cl.CountryCode
where cl.Percentage >= all
(select sub.Percentage
from countrylanguage sub
where sub.CountryCode = cl.CountryCode)
  order by c.Name;

-- piu parlata x nazione 
select 
c.Name as Nazione,
cl.Language,
cl.Percentage
from country c 
join countrylanguage cl on c.Code = cl.CountryCode
where cl.Percentage >= all
(select sub.Percentage
from countrylanguage sub
where sub.CountryCode = cl.CountryCode)
and cl.Percentage =
(select max(innercl.Percentage)
from countrylanguage innercl
where innercl.CountryCode = cl.CountryCode)
having cl.Percentage > any
(select sub2.Percentage 
from countrylanguage sub2
where sub2.Percentage < 100)
order by c.Name;
