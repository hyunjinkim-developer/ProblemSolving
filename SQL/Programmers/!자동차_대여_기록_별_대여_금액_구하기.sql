-- Problem: https://school.programmers.co.kr/learn/courses/30/lessons/151141

-- 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서
-- 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여
-- 대여 기록 ID와 대여 금액 리스트를 출력
-- 결과는 대여 금액을 기준으로 내림차순 정렬하고,
-- 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬

-- IFNULL(expression, alternative_value)
-- returns a specified value if the expression is NULL

SELECT
    H.HISTORY_ID
    , FLOOR(C.DAILY_FEE
            * (DATEDIFF(H.END_DATE, H.START_DATE) + 1)
            * (1 - IFNULL(P.DISCOUNT_RATE, 0) / 100))
        AS FEE
FROM CAR_RENTAL_COMPANY_CAR C
INNER JOIN
    CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
LEFT JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
        ON C.CAR_TYPE = P.CAR_TYPE
            AND P.DURATION_TYPE = (
                CASE
                    WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN "90일 이상"
                    WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN "30일 이상"
                    WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN "7일 이상"
                END
            )
WHERE C.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC