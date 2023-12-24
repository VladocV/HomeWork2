import pandas as pd

df = pd.read_csv('/content/Customers.csv', delimiter=';')

df[(df['Age'] > 30) & (df['Income'] < 30000)]

df[(df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]
