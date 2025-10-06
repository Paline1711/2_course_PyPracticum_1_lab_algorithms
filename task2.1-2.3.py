
import pandas as pd

# Загрузка данных (пример с данными Titanic)
df = pd.read_csv('titanic.csv')

# 1. Заполнение пропусков в Age медианным значением  
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# Проверка, что пропусков больше нет  
print("Информация о данных после заполнения пропусков:")
print(df.info())

# 2. Создание функции для возрастных групп  
def get_age_group(age):
    """Функция для определения возрастной группы"""
    if age < 18:
        return "Ребенок"
    elif 18 <= age <= 65:
        return "Взрослый"
    else:
        return "Пожилой"

# 3. Добавление столбца AgeGroup и применение функции  
df['AgeGroup'] = df['Age'].apply(get_age_group)

# Вывод первых 10 строк для проверки  
print("\nПервые 10 строк с возрастом и возрастной группой:")
print(df[['Age', 'AgeGroup']].head(10))
