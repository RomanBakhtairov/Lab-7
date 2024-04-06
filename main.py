import numpy as np
import matplotlib.pyplot as plt
import time as tm
from mpl_toolkits.mplot3d import Axes3D
import random as rd
#Каждый метод есть в функции start на строке 77
#Я взял вариант № 2
##Задание №1, проверка работы numpy
def numPyTest():
    nparray = np.random.randint(1,100,size=2000000)
    pyarray = [rd.randint(1,100) for i in range(2000000)]
    #
    nA,nB = [nparray[:1000000], nparray[1000000:]]
    pA,pB = [pyarray[:1000000], pyarray[1000000:]]
    #
    def timer(func,a,b):
        time = tm.perf_counter()
        func(a,b)
        return tm.perf_counter() - time
    def multiplyarray(a,b):
        return [a[i] * b[i] for i in range(len(a))]
    #
    timeN = timer(np.multiply, nA,nB)
    timeP =  timer(multiplyarray,pA,pB)
    print(f"Время умножения в NumPy: {timeN}")
    print(f'Время умножения в python:{timeP}')
    print(f'Numpy быстрее стандарта в {round(timeP/timeN)} раза')
#Задание №2, построение гистограммы 
def myHist():
    arr = np.genfromtxt('data2.csv', delimiter=',')
    arr = arr[1:]
    pH = (arr[:,0])
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.set_xlabel('pH')
    ax.set_ylabel('Частота')
    ax.set_title(f'гистограмма для параметра pH \n среднеквадратичное отклонение:{np.std(np.nan_to_num(pH))}')
    ax.hist(pH, 16)
    ax.grid()
    plt.show()
#Задание №3, построение функции в 3D
def drow3D_function():
      x_value = np.linspace(-2*np.pi,2*np.pi, 100)
      y_value = np.sin(x_value)*np.cos(x_value)
      z_value = np.sin(x_value)*np.cos(x_value)
      frame = plt.figure()
      ax = frame.add_subplot(111, projection='3d')
      ax.plot(x_value, y_value, z_value, marker='x', c='red')
      plt.show()          
#Доп задание
def move_graph_version1():
    x_value = [0]
    y_value = [0]
    for i in range(50):
        x_value.append(x_value[-1]+0.2)
        y_value.append(np.sin(x_value[-1]))
        plt.xlim(0,10)
        plt.ylim(-2, 2)
        plt.scatter(x_value, y_value,color = 'black')
        plt.pause(0.0001)
    plt.show()
def move_graph_version2():
    x_value = np.linspace(-10,10,40)
    edit_x = x_value
    y_value = np.sin(x_value)
    for i in range(100):
        plt.clf()
        edit_x = edit_x +0.2 
        y_value= np.sin(edit_x)
        plt.xlim(0,10)
        plt.ylim(-2, 2)
        plt.scatter(x_value, y_value,color = 'black')
        plt.pause(0.0001)
    plt.show()

def Start():
#Задание 1

    #numPyTest()

#Задание 2

    #myHist()

#Задание 3

    #drow3D_function()

#Доп задание(в 2 вариантах)

    #move_graph_version1()
    #move_graph_version2()
    pass
Start()