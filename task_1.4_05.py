
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 5. Раздел 1.4')
source_ls = ['2018-01-01', 'yandex', 'cpc', 100]
print(f'\n Исходные данные:\n source_ls: {source_ls}')
print('\n Вывод:')
if len(source_ls) >= 2:
    '''                                                               # Мой вариант
    my_val = source_ls[-1]
    for my_key in source_ls[-2::-1]:
        my_dict = {my_key: my_val}
        my_val = my_dict
    '''
    '''                                    # Вариант проверившего, Александр Бардин
    my_dict = {source_ls[-2]: source_ls[-1]}  # объявляю словарь, где ключ - [-2] элемент списка, а значение - [-1]
    for key in source_ls[:-2][::-1]:  # в обратном порядке, оставшиеся элементы списка, добавляю в словарь, в качестве ключа
        my_dict = {key: my_dict}      # в качестве значения, указываю имеющийся словарь
    '''
                                        # Мне понравился некий сембиоз: вариант Александра Бардина,
                                        # но с присутствием промежуточной переменной my_val.
    my_dict = {source_ls[-2]: source_ls[-1]}
    for key in source_ls[:-2][::-1]:
        my_val = my_dict
        my_dict = {key: my_val}
    
    print(f' my_dict:   {my_dict}')
else:
    print('\n В заданном списке меньше двух элементов.\n Словарь создать невозможно')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
