-- CAR_RENTAL_COMPANY_CAR 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차
-- 자동차 종류 별로 몇 대
-- 자동차 수에 대한 컬럼명은 CARS로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬

SELECT CAR_TYPE, COUNT(CAR_ID) AS "CARS"
FROM CAR_RENTAL_COMPANY_CAR
-- There's only 3_Greedy "시트" which is 통풍시트', '열선시트', '가죽시트'
-- the OPTIONS column consist of string, so "%시트%" is appropriate
WHERE OPTIONS LIKE "%시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC