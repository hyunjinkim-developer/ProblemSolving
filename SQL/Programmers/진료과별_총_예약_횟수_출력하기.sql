-- 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
-- 컬럼명은 '진료과 코드', '5월예약건수'로 지정해
-- 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬

SELECT MCDP_CD AS "진료과코드",
       COUNT(PT_NO) AS "5월예약건수"
FROM APPOINTMENT
WHERE "2022-05-01" <= APNT_YMD AND APNT_YMD <= "2022-05-31"
-- WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO) ASC, MCDP_CD ASC