SELECT d.id, d.name, d.budget, e.id employee_id, e.first_name, e.last_name, e.start_date, e.is_supervisor, e.department_id
FROM hrapp_department d
LEFT JOIN hrapp_employee e ON e.department_id = d.id
WHERE d.id = 1;

SELECT
    c.id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date
FROM hrapp_computer c
WHERE c.manufacturer = "apple";