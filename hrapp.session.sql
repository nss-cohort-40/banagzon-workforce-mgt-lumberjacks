SELECT d.id, d.name, d.budget, e.id, e.first_name, e.last_name, e.start_date, e.is_supervisor, e.department_id
FROM hrapp_department d
LEFT JOIN hrapp_employee e ON e.department_id = d.id;