import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def tableload():
    arr = np.genfromtxt('voltage.csv', delimiter = ',')
    print(arr)
    time = arr[:100,0]
    time = time[: np.newaxis]
    cuur = arr[:100,1]
    curr = time[: np.newaxis]
    volt = arr[:100,2] 
    volt = time[: np.newaxis]
    plt.plot(time,curr)
    plt.show()
def hist():
    arr = np.genfromtxt('test.csv', delimiter = ',')
    arr = arr[1:]
    age = np.int_(arr[:,1]/365.25)
    fig = plt.figure(figsize= (6,4))
    ax = fig.add_subplot()
    ax.hist(age,100)
    ax.grid()
    plt.show()
    
def plot3d():
    np.random.seed(40)
    xs = np.linspace(0, 10, 20)
    ys = xs
    zs = np.sin(xs)
    print(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()
#tableload()
plot3d()