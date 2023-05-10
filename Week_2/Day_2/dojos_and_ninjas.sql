CREATE DATABASE `dojos_and_ninjas_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

insert into dojos (name)
values ('Alpha');

insert into dojos (name)
values ('Bravo');

insert into dojos (name)
values ('Charlie');

delete from dojos
where name = 'Alpha';

delete from dojos
where name = 'Bravo';

delete from dojos
where name = 'Charlie';

insert into dojos (name)
values ('alpha');

insert into dojos (name)
values ('bravo');

insert into dojos (name)
values ('charlie');

insert into ninjas (dojos_id, first_name, last_name, age)
values (4, 'Harry', 'Potter', 21);

insert into ninjas (dojos_id, first_name, last_name, age)
values (4, 'Ron', 'Weasley', 22);

insert into ninjas (dojos_id, first_name, last_name, age)
values (4, 'Hermoine', 'Granger', 20);

insert into ninjas (dojos_id, first_name, last_name, age)
values (5, 'Naruto', 'Uzumaki', 18);

insert into ninjas (dojos_id, first_name, last_name, age)
values (5, 'Sasuke', 'Uchiha', 17);

insert into ninjas (dojos_id, first_name, last_name, age)
values (5, 'Sakura', 'Haruno', 17);

insert into ninjas (dojos_id, first_name, last_name, age)
values (6, 'Ichigo', 'Kurosaki', 29);

insert into ninjas (dojos_id, first_name, last_name, age)
values (6, 'Orihime', 'Inoue', 29);

insert into ninjas (dojos_id, first_name, last_name, age)
values (6, 'Rukia', 'Kuchiki', 129);

select *
from ninjas
where dojos_id = 4;

select *
from ninjas
where dojos_id = 6;

select *
from ninjas
join dojos on ninjas.id = 6;

select *
from dojos;

select *
from ninjas;