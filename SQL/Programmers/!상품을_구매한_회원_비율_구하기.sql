-- Interesting code convention

-- 2021년에 '가입'한 전체 회원들 중

-- 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력
-- 2021년에 가입한 회원 중 상품을 구매한 회원수 : (2021 가입) ^ (상품 구매) / (2021 가입)

-- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림
-- 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬

# Reference: https://blog.naver.com/deaf_52/223219593964

# Solution 1
SELECT
    BOUGHT.*
    , ROUND(BOUGHT.PURCHASED_USERS / USER_2021.COUNT, 1) AS PUCHASED_RATIO
FROM
    (
        SELECT
            YEAR(SALES.SALES_DATE) AS YEAR
            , MONTH(SALES.SALES_DATE) AS MONTH
            , COUNT(DISTINCT USERS.USER_ID) AS PURCHASED_USERS
        FROM
            USER_INFO USERS
            , ONLINE_SALE SALES
        WHERE
            USERS.USER_ID = SALES.USER_ID
            AND YEAR(USERS.JOINED) = 2021
        GROUP BY
            YEAR(SALES.SALES_DATE)
            , MONTH(SALES.SALES_DATE)
    ) BOUGHT
    , (
        SELECT COUNT(*) AS COUNT
        FROM USER_INFO USERS
        WHERE
            YEAR(JOINED) = 2021
    ) USER_2021
ORDER BY BOUGHT.YEAR ASC, BOUGHT.MONTH ASC

# # Solution 2
# # WITH Phrase is not recommended in performance-wise
# WITH USER_2021 AS (
#     SELECT COUNT(*) AS COUNT
#     FROM USER_INFO USERS
#     WHERE
#         YEAR(JOINED) = 2021
# )

# SELECT
#     YEAR(SALES.SALES_DATE) AS YEAR
#     , MONTH(SALES.SALES_DATE) AS MONTH
#     , COUNT(DISTINCT USERS.USER_ID) AS PUCHASED_USERS
#     , ROUND(COUNT(DISTINCT USERS.USER_ID) / (SELECT COUNT FROM USER_2021), 1) AS PUCHASED_RATIO
# FROM
#     USER_INFO USERS
#     , ONLINE_SALE SALES
# WHERE
#     USERS.USER_ID = SALES.USER_ID
#     AND YEAR(USERS.JOINED) = 2021
# GROUP BY
#     YEAR(SALES.SALES_DATE)
#     , MONTH(SALES.SALES_DATE)
# ORDER BY YEAR ASC, MONTH ASC