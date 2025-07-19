create or replace numero_ordini_clienteview numero_ordini_cliente as
select 
c.customerNumber,
c.customerName,
count(o.orderNumber) as numero_ordini
from
customers as c
left join
orders as o on c.customerNumber = o.customerNumber 
group by
c.customerNumber, c.customerName;


SELECT * FROM numero_ordini_cliente;
