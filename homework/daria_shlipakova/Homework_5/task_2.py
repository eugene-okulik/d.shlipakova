# срезы и метод index

line = 'результат операции: 42'
index_of_number = line.index(':') + 2
result = int(line[index_of_number:]) + 10
print(result)

line = 'результат операции: 514'
index_of_number = line.index(':') + 2
result = int(line[index_of_number:]) + 10
print(result)

line = 'результат работы программы: 9'
index_of_number = line.index(':') + 2
result = int(line[index_of_number:]) + 10
print(result)

# списки

line = 'результат операции: 42'
list_from_line = line.split()
result = int(list_from_line[-1]) + 10
print(result)

line = 'результат операции: 514'
list_from_line = line.split()
result = int(list_from_line[-1]) + 10
print(result)

line = 'результат работы программы: 9'
list_from_line = line.split()
result = int(list_from_line[-1]) + 10
print(result)
