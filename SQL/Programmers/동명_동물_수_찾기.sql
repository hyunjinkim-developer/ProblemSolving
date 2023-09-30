-- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
-- 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회

-- COUNT(NAME) VS COUNT(ANIMAL_ID)
-- 이름이 없는 동물은 집계에서 제외해달라고 했으므로, name 컬럼에는 null 데이터가 존재합니다.
-- 그런데 animal_id는 null 데이터의 존재여부를 알 수 없습니다. (아마도 null 데이터가 없을 것으로 예상됩니다.)
-- 그런데 'COUNT(컬럼)은 null 값을 제외하고 count를 하므로,'
-- count(name)과 count(animal_id)의 결과는 다를 것입니다.


SELECT NAME, COUNT(NAME) AS "COUNT"
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME