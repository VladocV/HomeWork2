import numpy as np

#вектор < 7
ar = np.random.randint(1, 10, size=100)
percent = sum(ar > 7)   #т.к len(ar) по условию =100, это сразу в %
print(percent, '%', sep= '')

#(ветор < 7)*1000 = 20%
i = 0
n = 0
while i < 1000:
  i += 1
  ar = np.random.randint(1, 10, size=100)
  percent = sum(ar > 7)
  if percent == 20:
    n += 1
print( f'{n} раз или {n/10}%')

#матрица 10*10, от 1 до 10
matrix = np.ones((10,10))
vector = np.array([0,1,2,3,4,5,6,7,8,9])
print(vector + matrix)

ar = np.random.randint(0, 9, size=100) #не понял какую матрицу
ar.resize(10,10)                       #поэтому создал 10*10 
print(ar.mean(axis=0))                 #из случайных чисел от 0 до 9
