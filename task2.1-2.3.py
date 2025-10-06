import pandas as pd
df = pd.read_csv('titanic.csv')
#Task 2.1
median_age = df['Age'].median()
print(f"Средний возраст: {median_age}")

print(df['Age'].fillna(median_age, inplace=True))

print("Информация о DataFrame после заполнения пропусков")
print(df.info())

#Task 2.2
def get_age_group(age):
    if age>18:
        return(Child)
    elif 18 < Age <= 65:
        return

df['AgeGroup'] = [10, 11, 12]
print(df)