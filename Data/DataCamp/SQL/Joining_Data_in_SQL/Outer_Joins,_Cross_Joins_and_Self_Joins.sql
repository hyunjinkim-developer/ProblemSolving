-- Outer Joins, Cross Joins and Self Joins
-- https://app.datacamp.com/learn/courses/joining-data-in-sql


-- This is a LEFT JOIN, right?
SELECT
	c1.name AS city,
    code,
    c2.name AS country,
    region,
    city_proper_pop
FROM cities AS c1
-- Join right table (with alias)
LEFT JOIN countries AS c2
ON c1.country_code = c2.code
ORDER BY code DESC;



-- Building on your LEFT JOIN
SELECT region, AVG(gdp_percapita) AS avg_gdp
FROM countries AS c
LEFT JOIN economies AS e
USING(code)
WHERE year = 2010
GROUP BY region
-- Order by descending avg_gdp
ORDER BY avg_gdp DESC
-- Return only first 10 records
LIMIT 10;



-- Is this RIGHT?
-- when converting a LEFT JOIN to a RIGHT JOIN,
-- change both the type of join
-- and the order of the tables to get equivalent results
-- The order of fields you are joining ON still does not matter.
-- Modify this query to use RIGHT JOIN instead of LEFT JOIN

SELECT countries.name AS country, languages.name AS language, percent
FROM languages
RIGHT JOIN countries
USING(code)
ORDER BY language;



-- Comparing joins

-- Perform a full join with countries (left) and currencies (right).
-- Filter for the North America region or NULL country names.
SELECT name AS country, code, region, basic_unit
FROM countries
-- Join to currencies
FULL JOIN currencies
USING (code)
-- Where region is North America or null
WHERE region = 'North America'
	OR name IS NULL
ORDER BY region;

-- full join into a left join with the currencies
SELECT name AS country, code, region, basic_unit
FROM countries
-- Join to currencies
LEFT JOIN currencies
USING (code)
WHERE region = 'North America'
	OR name IS NULL
ORDER BY region;

-- Repeat the same query again, this time performing an inner join of countries with currencies.
SELECT name AS country, code, region, basic_unit
FROM countries
-- Join to currencies
INNER JOIN currencies
USING (code)
WHERE region = 'North America'
	OR name IS NULL
ORDER BY region;



-- Chaining FULL JOINs
SELECT
	c1.name AS country,
    region,
    l.name AS language,
	basic_unit,
    frac_unit
FROM countries AS c1
-- Full join with languages (alias as l)
FULL JOIN languages AS l
USING (code)
-- Full join with currencies (alias as c2)
FULL JOIN currencies AS c2
USING (code)
WHERE region LIKE 'M%esia';



-- Histories and languages
SELECT c.name AS country, l.name AS language
-- Inner join countries as c with languages as l on code
FROM countries AS c
INNER JOIN languages AS l
USING (code)
WHERE c.code IN ('PAK','IND')
	AND l.code in ('PAK','IND');

SELECT c.name AS country, l.name AS language
FROM countries AS c
-- Perform a cross join to languages (alias as l)
CROSS JOIN languages AS l
WHERE c.code in ('PAK','IND')
	AND l.code in ('PAK','IND');



-- Choosing your join
SELECT
	c.name AS country,
    region,
    life_expectancy AS life_exp
FROM countries AS c
-- Join to populations (alias as p) using an appropriate join
RIGHT JOIN populations AS p
ON c.code = p.country_code
-- Filter for only results in the year 2010
WHERE year = 2010
-- Sort by life_exp
ORDER BY life_expectancy ASC
-- Limit to five records
LIMIT 5;


-- Select aliased fields from populations as p1
SELECT p1.country_code, p1.size AS "size2010", p2.size AS "size2015"
-- Join populations as p1 to itself, alias as p2, on country code
FROM populations AS p1
INNER JOIN populations AS p2
USING (country_code)

-- Eliminate unwanted records using a calculated field
SELECT
	p1.country_code,
    p1.size AS size2010,
    p2.size AS size2015
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code
WHERE p1.year = 2010
-- Filter such that p1.year is always five years before p2.year
    AND p1.year = p2.year - 5