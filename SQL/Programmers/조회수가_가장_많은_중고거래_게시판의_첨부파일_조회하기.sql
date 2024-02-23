-- USED_GOODS_BOARD와 USED_GOODS_FILE 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
-- 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
-- 기본적인 파일경로는 /home/grep/src/
-- 게시글 ID를 기준으로 디렉토리가 구분
-- 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록 출력
-- 조회수가 가장 높은 게시물은 하나만 존재

-- Solution 1:
SELECT CONCAT("/home/grep/src/",
              board.BOARD_ID, "/",
              FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE file
JOIN (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
) board
ON file.BOARD_ID = board.BOARD_ID
ORDER BY FILE_ID DESC

/*
-- Solution 2:
    -- JOIN USING
    -- SET NEW COLUMN with SQL statement on WHERE clause
SELECT CONCAT("/home/grep/src/",
              BOARD_ID, "/",
              FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE JOIN USED_GOODS_BOARD USING(BOARD_ID)
WHERE VIEWS = (
                SELECT MAX(VIEWS)
                FROM USED_GOODS_BOARD
                )
ORDER BY FILE_ID DESC
 */