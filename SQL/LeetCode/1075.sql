-- query that reports the average experience years of all the employees for each project,
-- rounded to 2 digits

-- Solution 1
SELECT project_id, ROUND(total_experience_years / employee_number, 2) AS average_years
FROM (SELECT project_id, count(Project.employee_id) AS employee_number, SUM(experience_years) AS total_experience_years
  FROM Project
  LEFT JOIN Employee ON Project.employee_id = Employee.employee_id
  GROUP BY project_id) By_project

-- Solution 2
-- without subquery, calculate as experience_years' average per group
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id