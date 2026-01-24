/* 
.............................................................
-------------------------------------------------------------
creating  shift roaster for the employee
-------------------------------------------------------------
.............................................................
*/
-- creating new type variable for the our table user defined columne 
create type status as enum ('day','night' );
-- creating the table  to note the entries of employees for the shift 
create table employee_shift(id serial  , name varchar(40), phone_no int,shift status  , primary key(id , name));
select * from employee_shift;
-- inserting the the values into the table employee_shift 
insert into employee_shift(id, name, phone_no) values ('20','uday',08083038 ), ( '10','sai',0804747474);
insert into employee_shift(id, name, phone_no) values('20','gagan',08083038 ), ( '10','kiran',0804747474);

select * from employee_shift;
/* Oops! we found out that we have missed to entry the shift timeing for the each user in shift column while 
ingesting the data in to the table
we don't want to create the entire the scripts all over again . what could we do now ?
we can use the truncate function to just remove the entries in the table without droping or losing the table itself . 
so use the truncate to avoid writing all the previous scripts again */

-- truncate to remove the data in the table without droping the table itself
truncate table employee_shift;

select * from employee_shift;
-- re enter the entries in to table but this time with the shifts entries also be ingested 
insert into employee_shift(id, name, phone_no,shift) values ('20','uday',08083038 , 'night'), ( '10','sai',0804747474,'day');
insert into employee_shift(id, name, phone_no,shift) values('20','gagan',08083038 , 'night' ), ( '10','kiran',0804747474, 'day');

select * from employee_shift;


/*

============================================================================
creating the table to entry the student absent or present on day per week1-4
============================================================================
*/

create type weeks as enum('week1','week2','week3','week4');
create type attandence as enum ( 'present','absent');


create table student_attendance(id varchar(10), name varchar(50), parents_no bigint, week weeks , attendance attandence,attendance_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key (name, id,  attendance_date));

-- ALTER TABLE student_attendance ADD COLUMN attendance_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
-- alter table student_attendance add column att_date timestamp default current_timestamp;

insert into student_attendance(id, name, parents_no, week, attendance) values ('38', 'sai ram',7013751263, 'week1' , 'present'),
('17','gagan yanamangandla', 2020484940,'week1', 'absent'),
('11','sai kiran',2020484940,'week1', 'absent');

drop table student_attendance;


select * from student_attendance;

insert into student_attendance(id, name, parents_no, week, attendance,attendance_date) values ('38', 'sai ram',7013751263, 'week1' , 'present','24-01-2025'),
('17','gagan yanamangandla', 2020484940,'week1', 'absent','24-01-2025'),
('11','sai kiran',2020484940,'week1', 'absent','24-01-2025');
drop table student_attendance;


create table student_attendance(id varchar(10), name varchar(50), parents_no bigint, week weeks , attendance attandence,attendance_date DATE DEFAULT CURRENT_DATE, attendance_time time default current_time, primary key (name, id,  attendance_date));

insert into student_attendance(id, name, parents_no, week, attendance) values ('38', 'sai ram',7013751263, 'week1' , 'present'),
('17','gagan yanamangandla', 2020484940,'week1', 'absent'),
('11','sai kiran',2020484940,'week1', 'absent');

insert into student_attendance(id, name, parents_no, week, attendance,attendance_date) values ('38', 'sai ram',7013751263, 'week1' , 'present','24-01-2025'),
('17','gagan yanamangandla', 2020484940,'week1', 'absent','24-01-2025'),
('11','sai kiran',2020484940,'week1', 'absent','24-01-2025');

select * from student_attendance;

/*
=================================================================================
=================================================================================
*/
create table student_dt(id  varchar(30) primary key, name varchar(40), phone_no int );
select * from student_dt;
insert into student_dt(id, name, phone_no) values ('20','uday',08083038 ), ( '10','sai',0804747474);
insert into student_dt(id, name, phone_no) values('20','gagan',08083038 ), ( '10','hod',0804747474);



insert into student_d(id, name, phone_no) values ('20','uday',08083038 ), ( '10','sai',0804747474);
insert into student_d(id, name, phone_no) values('20','gagan',08083038 ), ( '10','kiran',0804747474);
select * from student_d;

drop table student_d;