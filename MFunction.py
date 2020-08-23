import numpy as np
import matplotlib.pyplot as plt

class MFunction:
    def __init__(self,equation):
        self.equation = "("+equation+")"
        self.h = 10**-8
    def __add__(self, other):
        return MFunction(str(self.equation) +"+"+ str(other.equation))
        
    def __sub__(self, other):
        return MFunction(str(self.equation) +"+ (-1*"+ str(other.equation)+")")
    def __mul__(self, other):
        return MFunction(str(self.equation) +"*"+ str(other.equation))
    def __truediv__(self, other):
        return MFunction(str(self.equation) +"/"+ str(other.equation))
    def call(self,x):
        return eval(self.equation)
    def __str__(self):
        return str(self.equation)
    def deriv(self,x):
        return (self.call(x+self.h)-self.call(x))/self.h
    def deriv_function(self):
        return MFunction(eval(("self.call(x+self.h)-self.call(x))/self.h")))
    def plot_deriv(self,x_min,x_max):
        x = np.linspace(x_min,x_max,1000)
        plt.plot(x,self.deriv(x))
        plt.show()
    def plot_graph(self,x_min,x_max):
        x = np.linspace(x_min,x_max,1000)
        plt.plot(x,self.call(x))
        plt.show()
