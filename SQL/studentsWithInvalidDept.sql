SELECT
  Students.id, Students.name
FROM
  Students
  LEFT OUTER JOIN
  Departments ON Students.department_id = Departments.id
WHERE
    Departments.name IS NULL