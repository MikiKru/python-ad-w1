CREATE DATABASE python_db;

create user 'python_user'@'localhost' identified by '123';
grant SELECT, UPDATE, DELETE, INSERT on python_db.* to 'python_user'@'localhost';

use python_db;
create table users(
	id int primary key auto_increment,
    name varchar(255) not null,
    lastname varchar(255) not null,
    birthdate date not null,
    salary double(8,2) not null,
    gender enum('M','K')
);

INSERT INTO `python_db`.`users` (`id`, `name`, `lastname`, `birthdate`, `salary`, `gender`) VALUES ('1', 'Marek', 'Kot', '2000-02-02', '4000', 'M');
INSERT INTO `python_db`.`users` (`id`, `name`, `lastname`, `birthdate`, `salary`, `gender`) VALUES ('2', 'Anna', 'Nowak', '1999-04-02', '3000', 'K');
INSERT INTO `python_db`.`users` (`id`, `name`, `lastname`, `birthdate`, `salary`, `gender`) VALUES ('3', 'Jan', 'Nowy', '1988-02-01', '5000', 'M');

SELECT * FROM python_db.users;