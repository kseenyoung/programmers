-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, LEFT(REVIEW_DATE, 10) REVIEW_DATE
FROM MEMBER_PROFILE P
JOIN REST_REVIEW R ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID = (
                    SELECT MEMBER_ID
                   FROM REST_REVIEW
                   GROUP BY MEMBER_ID
                   ORDER BY COUNT(*) DESC
                   LIMIT 1
                   )
ORDER BY 3, 2