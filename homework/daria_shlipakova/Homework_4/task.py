my_dict = {
    'tuple': (1, 2, 'pepe', 'pupu', False, 2.5),
    'list': [3, 4, 'dog', 4.5, 'doggo'],
    'dict': {'1': 5, '2': 6, '3': 7, '4': 8, '5': 9},
    'set': {10, 11, 12, 13, True}
}

last_element_tuple = my_dict['tuple'][-1]
print('Последний элемент кортежа: ', last_element_tuple)

my_dict['list'].append('added')
my_dict['list'].pop(1)

my_dict['dict'].update({('i am a tuple', ): 'no'})
my_dict['dict'].pop('5')

my_dict['set'].add(14)
my_dict['set'].discard(10)

print('Словарь: ', my_dict)
