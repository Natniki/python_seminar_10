#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
#которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
#Сможете ли вы это сделать без get_dummies?

#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI':lst})
#data.head()


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame()# Создаем пустой DataFrame

for unique_value in set(lst):# Создаем столбцы one-hot кодировки
    data[unique_value] = [1 if value == unique_value else 0 for value in lst]

print(data.head(10))# Выводим первые строки DataFrame