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
WHERE c.manufacturer LIKE '%ap%';

SELECT
    c.id computer_id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date,
    e.id,
    e.first_name,
    e.last_name
FROM hrapp_computer c
LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
LEFT JOIN hrapp_employee e ON e.id = ec.employee_id;

select
            c.id computer_id,
            ec.id employee_computer_id,
            c.make,
            c.manufacturer,
            c.purchase_date,
            c.decommission_date

        from hrapp_computer c
        left join hrapp_employeecomputer ec on ec.computer_id = c.id