-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물
-- 아이디와 생물 종, 이름을 조회
-- 아이디 순으로 조회

SELECT ANIMAL_INS.ANIMAL_ID AS ANIMAL_ID,
        ANIMAL_INS.ANIMAL_TYPE AS ANIMAL_TYPE,
        ANIMAL_INS.NAME AS NAME
FROM ANIMAL_INS
INNER JOIN ANIMAL_OUTS
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE (ANIMAL_INS.SEX_UPON_INTAKE LIKE "Intact%"
        AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE "Spayed%"
                OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE "Neutered%"))
ORDER BY ANIMAL_INS.ANIMAL_ID;