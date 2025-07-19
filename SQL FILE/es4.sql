select
c.customerNumber, c.customerName,

sum(od.quantityOrdered * od.priceEach) as totale_speso 
-- arrotonda il totale in 2 decimali
-- round(sum(od.quantityOrdered * od.priceEach), 2) as totale_speso
from
customers as c
join orders as o on c.customerNumber = o.customerNumber
join orderdetails as od on o.orderNumber = od.orderNumber

group by checkNumberid
c.customerNumber, c.customerName 
having
totale_speso > 100000
-- where totale_speso > 10000

order by
totale_speso desc
limit 5;