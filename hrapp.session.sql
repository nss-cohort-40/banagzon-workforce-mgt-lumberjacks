SELECT
    c.id computer_id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date,
    e.id employee_id,
    e.first_name,
    e.last_name
FROM hrapp_computer c
LEFT JOIN hrapp_employeecomputer ec ON ec.computer_id = c.id
LEFT JOIN hrapp_employee e ON e.id = ec.employee_id;

SELECT
    c.id,
    c.manufacturer,
    c.make,
    c.purchase_date,
    c.decommission_date
FROM hrapp_computer c

select
    e.id,
    e.first_name,
    e.last_name,
    e.start_date,
    e.is_supervisor,
    d.id department,
    c.id computer_id,
    c.make computer_make,
    c.manufacturer,
    ec.id employee_computer_id
    
from hrapp_employee e
left join hrapp_department d on e.department_id = d.id
left join hrapp_employeecomputer ec on ec.employee_id = e.id
left join hrapp_computer c on c.id = ec.computer_id

DELETE
FROM hrapp_computer
WHERE id = 11