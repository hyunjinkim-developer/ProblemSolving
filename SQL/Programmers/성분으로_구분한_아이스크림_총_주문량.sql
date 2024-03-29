-- 상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을
-- 총주문량이 작은 순서대로 조회
-- 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정

SELECT ICECREAM_INFO.INGREDIENT_TYPE AS INGREDIENT_TYPE,
        SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF
RIGHT JOIN ICECREAM_INFO
ON FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
GROUP BY ICECREAM_INFO.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC