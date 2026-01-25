-- creating new table 
create table uday1(task_name varchar(100) primary key ,task_date date default current_DATE,
entry_time timestamp default current_timestamp, entytime time default current_time,spent_hour int, mobile_no bigint, id serial );
-- THE TABLE UDAY1 already exist what should i do now ! 
-- no worries i can delete it and create new table with the same name if i want using "DROP" function
-- ============================================================================================
-- ---------------------------------DROP--------------------------------------------
-- ===========================================================================================

drop table uday1;
-- ===========================================================================================
-- -----------------------------------creating the table again--------------------------------
-- ===========================================================================================
create table uday1(task_name varchar(100) primary key ,task_date date default current_DATE,
entry_time timestamp default current_timestamp, entytime time default current_time,spent_hour int, mobile_no bigint, id serial );
-- ====================================view the table after creating============================================

select * from uday1;

-- the table is created now but it is empty what should i do now !
-- don't worry, we should ingestion the data in to the table 
insert into uday1(task_name,spent_hour,mobile_no,id) values ('studied python',2,9990200303,'1');

-- lets checkout the table after the entry in to table using the select functions

select * from uday1;

-- i want remove the data from the table but i don't want delete the table itself , what do i now !!! worried 😯
-- not worry, lets just the truncate fucntion it will not delete the table itself but just remove rows of the data from the table that's it 

truncate uday1;
select * from uday1;
-- now i can do more entries in to table which which ever i wwant 
insert into uday1
	(task_name,id,spent_hour,mobile_no)
values
	('talked with friend on call','1',1,08048048384),
	('doom scrolled for the litterly forverever', '2',4,9797977979),
	('i watched gagan firlting with girls , i think he crazy for girls','1',3,04309499434);


insert into uday1
	(task_name,id,spent_hour)
values
	('talked with friends on call','1',1);

	select * from uday1;
-- i want to delete 1 specific row from the table , cause i made it for fun now i need to upload it to my git hub repo 
-- what do i do now !
-- don't worry lets use the 'delete' to remove row from table function
-- ============================= DELETE========================================================
delete from uday1 where task_name ='i watched gagan firlting with girls , i think he crazy for girls';

select * from uday1;
delete from uday1 where task_name='talked with friends on call';
select * from uday1;
-- ho no i forgot that i don't need the mobile_no column at all it is useless for me , what should i do 
-- should drop the table table and start whole process again 😢!
-- don't worry my man , i got you covered . Use the ALTER function to make changes to the existing table 
-- without removing any other data or  droping the table itself . let me show it you 

alter table uday1 drop column mobile_no;

select * from uday1;

alter table uday1 add column priority varchar(7);
select * from uday1;

alter table uday1 rename column priority to priority_level;
select * from uday1;
ALTER TABLE uday1 ALTER COLUMN priority_level TYPE VARCHAR(15);
-- alter table uday1 alter column priority_level type int using priority_level :: int;
select * from uday1;


-- i want to change the date of the task i have entried in to table without deleting it can i do it !
-- yes buddy you can use the Update function to update the existing row values 
update uday1 set task_date = '2026-01-24' where  task_name = 'talked with friend on call';

select * from uday1;