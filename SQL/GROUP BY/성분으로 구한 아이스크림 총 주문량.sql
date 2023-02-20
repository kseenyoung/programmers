SELECT ingredient_type, sum(total_order)
FROM FIRST_HALF f
JOIN ICECREAM_INFO i ON f.flavor = i.flavor
GROUP by 1
order by 2