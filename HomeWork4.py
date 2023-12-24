import pandas as pd

#чтение датасета
df = pd.read_csv('/content/Customers.csv', delimiter=';')

#поиск людей у которых возраст больше 30 и доход меньше 30000
df[(df['Age'] > 30) & (df['Income'] < 30000)]

#поиск людей, которые по профессии юристы с опытом работы больше 5 лет
df[(df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]
