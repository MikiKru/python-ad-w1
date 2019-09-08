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