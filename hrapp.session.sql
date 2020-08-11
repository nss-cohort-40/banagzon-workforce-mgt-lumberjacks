SELECT d.id, d.name, d.budget, e.first_name, e.last_name
FROM hrapp_department d
LEFT JOIN hrapp_employee e ON e.department_id = d.id;