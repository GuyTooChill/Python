CREATE DATABASE `users_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
SET SQL_SAFE_UPDATES = 0;

ALTER TABLE users MODIFY id int NOT NULL AUTO_INCREMENT;

insert into users (first_name, last_name, email)
values('Diego', 'Gonzalez', 'diego1234@gmail.com');

insert into users (first_name, last_name, email)
values ('John', 'Calixte', 'john1234@gmail.com');

insert into users (first_name, last_name, email)
values ('Mario', 'Aparicio', 'mario1234@gmail.com');

select *
from users;

select *
from users
where email = 'diego1234@gmail.com';

select *
from users
where id = 3;

update users
set last_name = 'Pancakes'
where id = 3;

delete from users
where id = 2;

select *
from users
order by first_name desc;