# Rastislav Petras
# 21 March 2020
# Excercise 8 
# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np  # required library for power of function and linspace function
import matplotlib.pyplot as plt # plotting library

x = np.linspace(0,4,100)  # Returns num evenly spaced samples, calculated over the interval      
f = x      # function f(x)=x
g = x**2   # function g(x)=x2
h = x**3   # function h(x)=x3
plt.plot(x,f, 'r')  # plot function f with red colour
plt.plot(x,g, 'g')  # plot function g with green colour
plt.plot(x,h, 'b')  # plot function h with blue colour
plt.ylabel('value of function (f/g/h)')  # label y axis
plt.xlabel('value of x')      # label x axis
plt.title("Mat-lab excercise")  # print title label
plt.savefig("Excercise_8.png")  # save ploting figure as Excercise_8.png in local directory

#End of excercise