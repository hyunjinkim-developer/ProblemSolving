SELECT FLAVOR
FROM (SELECT FIRST_HALF.FLAVOR AS FLAVOR, FIRST_HALF.TOTAL_ORDER + JULY.TOTAL_ORDER AS TOTAL_ORDER
      FROM FIRST_HALF
      LEFT JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
                 FROM JULY
                 GROUP BY FLAVOR) JULY
      ON FIRST_HALF.FLAVOR = JULY.FLAVOR) TOTAL
ORDER BY TOTAL.TOTAL_ORDER DESC
LIMIT 3;