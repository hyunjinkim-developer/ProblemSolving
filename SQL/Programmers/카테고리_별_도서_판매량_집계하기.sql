-- 2022년 1월의 카테고리 별 도서 판매량을 합산
-- 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력
-- 결과는 카테고리명을 기준으로 오름차순 정렬

SELECT BOOK.CATEGORY AS CATEGORY
        , SUM(BOOK_SALES_2022JAN.SALES) AS TOTAL_SALES
FROM (SELECT BOOK_ID, SUM(SALES) AS SALES
      FROM BOOK_SALES
      WHERE SALES_DATE LIKE "2022-01-%"
      GROUP BY BOOK_ID) BOOK_SALES_2022JAN
INNER JOIN BOOK
ON BOOK.BOOK_ID = BOOK_SALES_2022JAN.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY ASC