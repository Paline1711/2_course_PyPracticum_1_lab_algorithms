import pandas as pd
df = pd.read_csv('C:\\Users\\1132243257\\PycharmProjects\\lab1_pandas\\.venv\\titanic.csv')
print(df.head(7))
print("info")
print(df.info())
# Пропущенные значения есть в 4 и 7 строке (тип данных float 64)
data_age = df['Age'].describe()

print(data_age)

# Fare_max= 512.32920,mean_age = 29.471443