CREATE TABLE student_attendance (
    id VARCHAR(10),
    name VARCHAR(50),
    parents_no BIGINT,
    week weeks,
    attendance status,
    attendance_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id, name, attendance_date)
);
create type weeks as enum('week1','week2','week3','week4');
create type status as enum ( 'present','absent');
DROP TYPE status;
ALTER TYPE status ADD VALUE 'late';
CREATE TYPE status AS ENUM ('present','absent');

insert into student_attendance(id, name, parents_no, week, attendance) values ('38', 'sai ram',7013751263, 'week1' , 'present'),
('17','gagan yanamangandla', 2020484940,'week1', 'absent'),
('11','sai kiran',2020484940,'week1', 'absent');

drop table student_attendance;

DROP TYPE status CASCADE;