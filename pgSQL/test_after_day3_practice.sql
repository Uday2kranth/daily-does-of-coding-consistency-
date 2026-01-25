create type shifts as enum('day','night');
create table employee_t(emp_id varchar(10) ,name varchar(40), 
mobile_no bigint,working_hours int ,shifts shifts, primary key(emp_id,name));

select * from employee_t;
alter table employee_t rename column name to emp_name;

insert into  employee_t(emp_id,shifts, emp_name,working_hours , mobile_no) values ('emp_007','day', 'rufus', 8, 0908328383083);

select * from employee_t;

insert into employee_t(emp_id,shifts,emp_name,working_hours,mobile_no)
values('emp_007','night','dongrees',9,0388383838),('emp_007','day','barepuk',9,708708038038);
select * from employee_t;

update employee_t set emp_id ='emp_001' where emp_id ='emp_007' and emp_name='barepuk';
insert into employee_t(emp_id,emp_name) values ('emp_000','la pasion');

select * from employee_t;

delete from employee_t where emp_id='emp_000' and emp_name='la pasion';

select * from employee_t;

truncate employee_t;

select * from employee_t;
alter table employee_t add column experience  varchar(30);

select * from employee_t;

drop table employee_t;

select * from employee_t;