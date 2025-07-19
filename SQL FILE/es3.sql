/*select  country.Name AS Nazione,
  COUNT(city.ID) as NumeroCitta
from country
join
  city on country.Code = city.CountryCode
group by 
  country.Code, country.Name
order by 
  NumeroCitta desc;*/
  
  
select
country.Name as Nazione,
count(city.ID) as NumCitta

from country
left join 
city on country.Code = city.CountryCode
group by 
country.Code, country.Name
order by
NumCitta desc;



SELECT c.Name AS Paese, c.LifeExpectancy AS AspettativaVita, cl.Language AS Lingua
FROM world.country c
JOIN world.countrylanguage cl ON c.Code = cl.CountryCode
WHERE c.GovernmentForm LIKE '%Republic%' AND c.LifeExpectancy > 70 -- AND cl.IsOfficial = 'T';
