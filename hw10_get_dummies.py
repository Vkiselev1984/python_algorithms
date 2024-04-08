#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид. 
#Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
from tabulate import tabulate

# Генерация исходных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print("Исходный DataFrame:")
print(tabulate(data.head(), headers='keys', tablefmt='psql'))

# Преобразовываем столбец 'whoAmI' в one hot вид:
categories = data['whoAmI'].unique()
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

data = data.drop('whoAmI', axis=1)

print("\nDataFrame после преобразования в one hot вид:")
print(tabulate(data.head(), headers='keys', tablefmt='psql'))