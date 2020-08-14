SELECT
    e.id,
    e.first_name,
    e.last_name,
    ec.computer_id,
    ec.unassign_date
FROM hrapp_employee e
LEFT JOIN hrapp_employeecomputer ec ON ec.employee_id = e.id
WHERE ec.unassign_date ISNULL