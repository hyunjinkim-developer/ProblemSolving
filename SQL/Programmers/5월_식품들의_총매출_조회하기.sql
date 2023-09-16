-- 생산일자가 2022년 5월인 식품들의 
-- 식품 ID, 식품 이름, 총매출을 조회
-- 총매출을 기준으로 내림차순 정렬/ 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬

SELECT MAY_PRODUCED.PRODUCT_ID AS PRODUCT_ID, 
        FOOD_PRODUCT.PRODUCT_NAME AS PRODUCT_NAME,
        MAY_PRODUCED.AMOUNT * FOOD_PRODUCT.PRICE AS TOTAL_SALES
FROM FOOD_PRODUCT
INNER JOIN (SELECT ORDER_ID, PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
            FROM FOOD_ORDER
            WHERE FOOD_ORDER.PRODUCE_DATE BETWEEN "2022-05-01 00:00:00" AND "2022-05-31 00:00:00"
            -- same product can be ordered several times
            GROUP BY PRODUCT_ID) MAY_PRODUCED 
ON FOOD_PRODUCT.PRODUCT_ID = MAY_PRODUCED.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;