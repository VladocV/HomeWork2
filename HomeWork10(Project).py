import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Housing.csv') #, delimiter=';')
missing_values = df.isnull().sum() #пропусков нет

#part 1:
grouped_data1 = df.groupby('price')['bedrooms'].min().reset_index()
# Самый дешевый: 1 750 000, кол-во спален: 2
grouped_data2 = len(df[df['bedrooms'] <= df['bathrooms']])
# Ответ: 15
grouped_data3 = df[df['guestroom'] == 'yes']['price'].min()
# Ответ: 2450000
df_filter4 = df[(df['price'] <= 2000000) | (df['price'] >= 5000000)]
df_aircond4 = df_filter4[df_filter4['airconditioning'] == 'yes']
grouped_data4 =  round((len(df_aircond4) / len(df_filter4)) * 100, 1)
# Ответ: 53.92%

#part 2:
color = {0 : 'black', 1 : 'red', 2: 'green', 3: 'blue'}
plt.scatter(df['price'], df['area'], c=df['parking'].map(color), marker = '1', alpha=0.5)
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.title('График Цена/Площадь')
plt.grid(True)
plt.show()

#part 3:
fig, axes = plt.subplots(2,2, figsize=(14,8))
axes[0,0].scatter(df['price'], df['area'], c=df['guestroom'].map({'yes' : '#CC9900', 'no' : '#009999'}), marker = 'D', s=15, alpha=0.4)
axes[0,0].set_title('Цена/Площадь + гостевая комнота', fontsize= 10)
axes[0,0].set_xlabel('Цена', fontsize= 8)
axes[0,0].set_ylabel('Площадь', fontsize= 8)
axes[0,0].grid(True)
axes[0,1].scatter(df['price'], df['area'], c=df['basement'].map({'yes' : '#006600', 'no' : '0.2'}), marker = 'p', s=25, alpha=0.4)
axes[0,1].set_title('Цена/Площадь + подвал', fontsize= 10)
axes[0,1].set_xlabel('Цена', fontsize= 8)
axes[0,1].set_ylabel('Площадь', fontsize= 8)
axes[0,1].grid(True)
axes[1,0].scatter(df['price'], df['area'], c=df['hotwaterheating'].map({'yes' : '#cc0000', 'no' : '#2567FF'}), marker = 'P', s=25, alpha=0.4)
axes[1,0].set_title('Цена/Площадь + отопление', fontsize= 10)
axes[1,0].set_xlabel('Цена', fontsize= 8)
axes[1,0].set_ylabel('Площадь', fontsize= 8)
axes[1,0].grid(True)
axes[1,1].scatter(df['price'], df['area'], c=df['prefarea'].map({'yes' : '#ff8000', 'no' : '#6600cc'}), marker = 'h', s=20, alpha=0.5)
axes[1,1].set_title('Цена/Площадь + предбанник', fontsize= 10)
axes[1,1].set_xlabel('Цена', fontsize= 8)
axes[1,1].set_ylabel('Площадь', fontsize= 8)
axes[1,1].grid(True)
plt.show()

#part 4:
with_aircond = df[df['airconditioning'] == 'yes']
no_aircond = df[df['airconditioning'] == 'no']
plt.hist(with_aircond['price'], color = 'lightgreen', edgecolor = 'g', bins = 25, label='С кондиционером')
plt.hist(no_aircond['price'], color = 'skyblue', edgecolor = 'b', bins = 25, alpha= 0.5, label='Без кондиционера')
plt.title('Распределение цены от наличия кондиционирования')
plt.legend()
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()
