-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일 출력
-- 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬

-- Reference: https://solo-superstar.tistory.com/entry/MySQL-OVER
SELECT MEMBER_NAME, REVIEW_TEXT,
        DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE
JOIN (SELECT MEMBER_ID, REVIEW_TEXT, REVIEW_DATE,
        COUNT(MEMBER_ID) OVER (PARTITION BY MEMBER_ID) AS REVIEW_COUNT
      FROM REST_REVIEW) COUNT_REVIEW
ON MEMBER_PROFILE.MEMBER_ID = COUNT_REVIEW.MEMBER_ID
WHERE REVIEW_COUNT = (SELECT COUNT(*)
                      FROM REST_REVIEW
                      GROUP BY MEMBER_ID
                      ORDER BY COUNT(*) DESC
                      LIMIT 1)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;