-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM
    (SELECT ANIMAL_ID, ANIMAL_TYPE, NAME, SEX_UPON_INTAKE
    FROM ANIMAL_INS
    WHERE SEX_UPON_INTAKE LIKE 'INTACT%'
     ) I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE SEX_UPON_OUTCOME LIKE 'SPAYED%'
OR SEX_UPON_OUTCOME LIKE 'Neutered%'
ORDER BY I.ANIMAL_ID
