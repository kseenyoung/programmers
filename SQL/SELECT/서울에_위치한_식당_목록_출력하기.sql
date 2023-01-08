SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, round(avg(b.review_score), 2) as SCORE
from REST_INFO a inner join REST_REVIEW b on a.REST_ID = b.REST_ID
where address like '서울%'
group by a.rest_id
order by score desc, FAVORITES desc;