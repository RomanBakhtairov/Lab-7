import numpy as np
import matplotlib.pyplot as plt
import time as tm
from mpl_toolkits.mplot3d import Axes3D
import random as rd
#Я взял вариант № 2
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
    print(f"Время умножения в NumPy: {tN}")
    print(f'Время умножения в python:{tP}')
    print(f'Numpy быстрее стандарта в {round(tP/tN)} раза')
    

numPyTest()
   
def updatedata() -> np.ndarray:
    filedata = np.genfromtxt('data1.csv', delimiter=',')
    #
    return 





# def start():
#     arr = np.array([5, 9, 10, 'ad', 7])
#     arr = arr[::-1]
#     print(arr)


# def tableLoad():
#     arr = np.genfromtxt('voltage.csv', delimiter=',')
#     time = arr[:100,0]
#     time = time[:,np.newaxis]
#     curr = arr[:100,1]
#     curr = curr[:,np.newaxis]
#     volt = arr[:100,2]
#     volt = volt[:,np.newaxis]

#     plt.plot(time, curr * 50, 'b', time, volt, 'r')
#     plt.show()


# def hist():
#     arr = np.genfromtxt('test.csv', delimiter=',')
#     arr = arr[1:]
#     daysInYear = 365.25

#     age = np.int_(arr[:,1] / daysInYear)

#     fig = plt.figure(figsize=(6, 4))
#     ax = fig.add_subplot()
#     ax.hist(age, 100, (50, 60))
#     ax.grid()
#     plt.show()


# def plot3d():
#     np.random.seed(40)
#     xs = np.linspace(0, 10, 20)
#     ys = xs
#     zs = np.sin(xs)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot(xs, ys, zs, marker='x', c='red')
#     plt.show()


# if __name__ == '__main__':
#     #start()
#     tableLoad()
#     #hist()
#     #plot3d()