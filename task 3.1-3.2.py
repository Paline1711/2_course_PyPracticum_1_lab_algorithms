import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
survival_by_sex = df.groupby('Sex')['Survived'].mean()
print("Процент выживших по полу:")
print(survival_by_sex)

# 2. Процент выживших в каждом классе
survival_by_class = df.groupby('Pclass')['Survived'].mean()
print("Процент выживших по классу:")
print(survival_by_class)

# 3. Сводная таблица: пол и класс
survival_pivot = df.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean')
print("Процент выживших в зависимости от пола и класса:")
print(survival_pivot)

# Задание 3.2: Фильтрация и сортировка
# 1. Несовершеннолетние из 3-го класса, которые выжили
filtered_1 = df[(df['Age'] < 18) & (df['Pclass'] == 3) & (df['Survived'] == 1)]
result_1 = filtered_1[['Name', 'Age']].sort_values('Age', ascending=False) # Сортируем по убыванию возраста
print("Несовершеннолетние выжившие из 3-го класса:")
print(result_1)

# 2. Самый пожилой мужчина, который не выжил
filtered_2 = df[(df['Sex'] == 'male') & (df['Survived'] == 0)]
oldest_male_not_survived = filtered_2.nlargest(1, 'Age')[['Name', 'Age']] # Находим строку с максимальным возрастом
print("Самый пожилой мужчина, который не выжил:")
print(oldest_male_not_survived)