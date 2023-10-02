-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여,
-- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
-- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬

SELECT BOOK_WITH_AUTHOR.AUTHOR_ID AS AUTHOR_ID,
        BOOK_WITH_AUTHOR.AUTHOR_NAME AS AUTHOR_NAME,
        BOOK_WITH_AUTHOR.CATEGORY AS CATEGORY,
        SUM(sales * price) AS TOTAL_SALES
FROM (SELECT *
      FROM BOOK_SALES
      WHERE SALES_DATE LIKE "2022-01-%") SALES_JAN
LEFT JOIN (SELECT BOOK.author_id AS author_id,
            author_name, book_id, category, price
           FROM AUTHOR
           INNER JOIN BOOK
           ON AUTHOR.AUTHOR_ID = BOOK.AUTHOR_ID) BOOK_WITH_AUTHOR
ON SALES_JAN.BOOK_ID = BOOK_WITH_AUTHOR.BOOK_ID
GROUP BY author_name, category
ORDER BY AUTHOR_ID ASC, CATEGORY DESC