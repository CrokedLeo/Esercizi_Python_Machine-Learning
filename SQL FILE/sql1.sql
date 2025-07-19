-- lingue x citta 
SELECT 
  ci.Name as Citta,
  co.Name as Nazione,
  cl.Language as Lingua
from city ci
join country co on ci.CountryCode = co.Code
join countrylanguage cl on co.Code = cl.CountryCode;

-- N citta x nazione
select 
  co.Name as Nazione,
  count(ci.ID) as NumeroCitta
from country co
join city ci on co.Code = ci.CountryCode
group by co.Name
order by NumeroCitta desc;

-- rep x vita > 70
select 
  co.Name as Nazione,
  co.GovernmentForm as Governo,
  co.LifeExpectancy as AspettativaVita,
  cl.Language as Lingua
from country co
join countrylanguage cl on co.Code = cl.CountryCode
where co.GovernmentForm like '%Republic%'
  and co.LifeExpectancy > 70;

-- citta=nome
select 
  ci.Name as Citta,
  co.Name as Nazione
from city ci
join country co on ci.CountryCode = co.Code;

-- left join
select 
  co.Name as Nazione,
  ci.Name as Citta
from country co
left join city ci on co.Code = ci.CountryCode;

-- tab lingua x nazioni
select 
  cl.Language,
  co.Name as Nazione
from countrylanguage cl
cross join country co;

-- tab nazioni no citta
select 
	co.Name as Nazione
from country co
left join city ci on co.Code = ci.CountryCode
where ci.ID is null;

