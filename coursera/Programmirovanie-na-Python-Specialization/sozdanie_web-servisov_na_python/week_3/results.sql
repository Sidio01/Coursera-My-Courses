use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * 
from product

-- 2. Выбрать названия всех автоматизированных складов
SELECT name 
FROM store

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT sum(total) 
FROM sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT store_id 
FROM sale 
group by store_id

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select distinct store.store_id 
from store 
left join sale 
on store.store_id = sale.store_id 
where quantity is null

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select distinct name, avg(total/quantity) 
from product p 
join sale s 
on p.product_id = s.product_id 
group by name

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select p.name	
from sale s  
join product p on p.product_id = s.product_id 
group by s.product_id
having count(distinct s.store_id) = 1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select st.name
from store st
join sale s
on st.store_id = s.store_id
group by s.store_id
having count(distinct s.product_id) = 1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select *  
from sale s 
order by total desc 
limit 1

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date
from sale s
group by date
order by sum(total) desc
limit 1
