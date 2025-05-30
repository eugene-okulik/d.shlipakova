-- 1) Создайте студента (student)

insert into students (name, second_name) values ('John', 'Doe');

-- 2) Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

insert into `books` (title, taken_by_student_id) values 
('Circles of Life of John Doe. Part 1', 20527),
('Circles of Life of John Doe. Part 2', 20527),
('Circles of Life of John Doe. Part 3', 20527);

-- 3) Создайте группу и определите своего студента туда

insert into `groups` (title, start_date, end_date) values ('John Doe himself', '01.01.2025', '01.01.2026');

update students set group_id = (select id from `groups` where title = 'John Doe himself') where id = 20527;

-- 4) Создайте несколько учебных предметов (subjects)

insert into subjets (title) values ('sub_1'), ('sub_2');

-- 5) Создайте по два занятия для каждого предмета (lessons)

insert into lessons (title, subject_id) values 
('lesson_1', 10818), 
('lesson_2', 10818), 
('lesson_1', 10819), 
('lesson_2', 10819);

-- 6) Поставьте своему студенту оценки (marks) для всех созданных вами занятий

insert into marks (value, lesson_id, student_id) values
('5', (select id from lessons where subject_id = 10818 and title = 'lesson_1'), 20527),
('5', (select id from lessons where subject_id = 10818 and title = 'lesson_2'), 20527),
('4', (select id from lessons where subject_id = 10819 and title = 'lesson_1'), 20527),
('4+', (select id from lessons where subject_id = 10819 and title = 'lesson_2'), 20527);

-- Получите информацию из базы данных:

-- 1) Все оценки студента

select value from marks where student_id = 20527;

-- 2) Все книги, которые находятся у студента

select title from books where taken_by_student_id = 20527;

-- 3) Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

select s.name as 'name', 
s.second_name as 'last name',
g.title as 'group', 
g.start_date as 'start date', 
g.end_date as 'end date', 
b.title as 'books', 
m. value as 'marks', 
l.title as 'lessons', 
sub.title as 'subjects'
from students s 
join `groups` g on s.group_id = g.id
join books b on s.id = b.taken_by_student_id
join marks m on s.id = m.student_id
join lessons l on m.lesson_id = l.id
join subjets sub on l.subject_id  = sub.id
where s.id = 20527;
