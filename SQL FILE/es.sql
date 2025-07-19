

-- create or replace view clienti_max_prodotti_diversi as

select 
c.customerNumber,
c.customerName,
max(prodotti_diversi) as max_prodotti_ordine
from(

-- SOTTO QUERY
select
o.customerNumber,
od.orderNumber,
count(distinct od.productCode) as prodotti_diversi
from
orders as o
join orderdetails as od on o.orderNumber = od.orderNumber
group by o.customerNumber, od.orderNumber

) as ordini_prodotti
join customers as c on ordini_prodotti.customerNumber = c.customerNumber 
group by
c.customerNumber, c.customerName
order by 
max_prodotti_ordine;

select * from clienti_max_prodotti_diversi
order by max_prodotti_ordine desc;


