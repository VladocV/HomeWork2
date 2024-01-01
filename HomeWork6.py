import matplotlib.pyplot as plt
import numpy as np


#график сложной алгебраической функции
def YFunc(X):
  return X + np.sin(X)**3/np.cos(X)

X = np.linspace(0, 10, 100)
Y = YFunc(X)
plt.plot(X, Y, color='g', dashes=[4,2],label='', alpha=0.75)
plt.title('Вот такая моя функция')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


#Скопление точек
X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
plt.scatter(X, Y, c='orange', s=50, alpha=0.5, marker='P')
plt.title('Скопление плюсов')
plt.legend('Точки')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.grid(True)
plt.show()


#Гистограмма результатов забега школьников
data = np.random.normal(16, 2, 1000)
plt.hist(data, bins=20, color='red', alpha=0.5)
plt.xlabel('Время забега')
plt.ylabel('Количество школьников')
plt.title('Результаты забега школьников на 100 метров')
plt.show()
#Выводы:
#1.Количество учеников с такм результатом, попадающих в каждый столбик, 
#  может быть оценено по высоте столбиков. 
#  Высокие столбики указывают на большую частоту значений в этом интервале.
#2.Распределение результатов имеет пик около значения 16, 
#  чем ближе к этому значению, тем больше таких результатов
