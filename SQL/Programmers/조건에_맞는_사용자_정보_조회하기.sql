-- 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력
-- 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
-- 결과는 회원 ID를 기준으로 내림차순 정렬

-- CONCAT(substring1, substring2, ...)
-- SUBSTRING(original_string, start, length)

SELECT
    USER_ID
    , NICKNAME
    , CONCAT(CITY, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2) AS "전체주소"
    , CONCAT(SUBSTRING(TLNO, 1, 3), "-", SUBSTRING(TLNO, 4, 4), "-", SUBSTRING(TLNO, 8, 4)) AS "전화번호"
FROM
    (
        SELECT *
        FROM USED_GOODS_BOARD BOARD
        LEFT JOIN USED_GOODS_USER USERS
        ON BOARD.WRITER_ID = USERS.USER_ID
        GROUP BY BOARD.WRITER_ID
        HAVING COUNT(BOARD.BOARD_ID) >= 3
    ) WRITERS
ORDER BY USER_ID DESC