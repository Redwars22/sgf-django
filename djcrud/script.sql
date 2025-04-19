CREATE TABLE `djcrud_employee` (
    `id` int(11) AUTO_INCREMENT PRIMARY KEY,
    `employee_id` varchar(20) NOT NULL,
    `employee_name` varchar(100) NOT NULL,
    `employee_email` varchar(100) NOT NULL,
    `employee_contacts` varchar(20) NOT NULL
);
