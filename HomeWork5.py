import pandas as pd

# Загрузка данных из датасета
df = pd.read_csv('/content/Customers.csv', delimiter=';')

# Удаление строк с пропусками
missing_values = df.isnull().sum()
df = df.dropna()

# Группировка и вычисление среднего дохода
income_profes = df.groupby('Profession')['Income'].mean()
income_profes = round(income_profes)
print(f'Средний годовой доход по профессиям:\n{income_profes}')
