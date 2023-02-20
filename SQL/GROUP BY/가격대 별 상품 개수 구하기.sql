SELECT truncate(price, -4) as PRICE_GROUP, count(*) PRODUCTS
FROM PRODUCT
group by 1
order by 1