from matplotlib import pyplot as plt
import numpy as np

def function_plt(start,end):
    x = np.arange(start*np.pi,end)
    y = np.sqrt(x)
    plt.title("function")
    plt.plot(x,y)
    plt.show()

function_plt(-100,100)

def scatter_plt():
    pass
def heatmap_plt():