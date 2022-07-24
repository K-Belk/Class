select * from classes

select name, credits from classes where credits > 3

select * from classes where mod(credits, 2) = 0

select * from 	students inner join enrollments on enrollments.student_id = students.id inner join classes on enrollments.class_id = classes.id where students.id = 1 and enrollments.grade is NULL

select * from 	students inner join enrollments on enrollments.student_id = students.id inner join classes on enrollments.class_id = classes.id where students.first_name = 'Tianna' and enrollments.grade is NULL

select * from students where 1986 > extract(year from birthdate)

select date_part('year',avg(age(birthdate))) from students 

select * from addresses where city ~ ' '

select first_name, last_name, line_1, city, state, zipcode from students inner join addresses on students.address_id = addresses.id where city ~ ' '

SELECT avg(credits) FROM classes

SELECT first_name, last_name from students inner join enrollments on enrollments.student_id = students.id where grade = 'A'

SELECT student_id, sum(credits) from students inner join enrollments on enrollments.student_id = students.id inner join classes on enrollments.class_id = classes.id where grade is not null GROUP BY student_id

select * from 	students inner join enrollments on enrollments.student_id = students.id inner join classes on enrollments.class_id = classes.id

select *  from 	students where date_part('year', birthdate) between '1982' and '1985'

INSERT INTO enrollments (student_id, class_id, grade) VALUES((select students.id from students where first_name = 'Andre' and last_name = 'Rohan'), (select classes.id from classes where name = 'PHYS 218'), 'A')