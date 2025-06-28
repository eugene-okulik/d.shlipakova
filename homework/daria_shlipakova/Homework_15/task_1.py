import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1) Создайте студента (student)

cursor.execute('insert into students (name, second_name) values (%s, %s)', ('John', 'Doe'))
student_id = cursor.lastrowid

# 2) Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

books_query = 'insert into `books` (title, taken_by_student_id) values (%s, %s)'
books_values = [
    ('Circles of Life of John Doe. Part 1', student_id),
    ('Circles of Life of John Doe. Part 2', student_id),
    ('Circles of Life of John Doe. Part 3', student_id)
]
cursor.executemany(books_query, books_values)

# 3) Создайте группу и определите своего студента туда

cursor.execute(
    'insert into `groups` (title, start_date, end_date) values (%s, %s, %s)',
    ('John Doe', '01.01.2025', '01.01.2026')
)
group_id = cursor.lastrowid
cursor.execute('update students set group_id = %s where id = %s', (group_id, student_id))

# 4) Создайте несколько учебных предметов (subjects)

cursor.execute("insert into subjets (title) values ('sub_1')")
subject1_id = cursor.lastrowid
cursor.execute("insert into subjets (title) values ('sub_2')")
subject2_id = cursor.lastrowid

# 5) Создайте по два занятия для каждого предмета (lessons)

lessons_query = 'insert into lessons (title, subject_id) values (%s, %s)'
lessons_values = [
    ('lesson_1', subject1_id),
    ('lesson_2', subject1_id),
    ('lesson_1', subject2_id),
    ('lesson_2', subject2_id)
]
lessons_ids = []
for value in lessons_values:
    cursor.execute(lessons_query, value)
    lessons_ids.append(cursor.lastrowid)

# 6) Поставьте своему студенту оценки (marks) для всех созданных вами занятий

marks_query = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
marks = ['5', '4', '3', '4+']
for mark, lesson_id in zip(marks, lessons_ids):
    cursor.execute(marks_query, (mark, lesson_id, student_id))

# Получите информацию из базы данных:
#
# 1) Все оценки студента

cursor.execute('select value from marks where student_id = %s', (student_id,))
marks = cursor.fetchall()

# 2) Все книги, которые находятся у студента

cursor.execute('select title from books where taken_by_student_id = %s', (student_id,))
books = cursor.fetchall()

# 3) Для вашего студента выведите всё, что о нем есть в базе

query = '''
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
where s.id = %s
'''
cursor.execute(query, (student_id,))
info = cursor.fetchall()

print(marks)
print(books)
print(info)

db.commit()
db.close()
