import sympy as sym
import numpy as np
import matplotlib.pyplot as plt 
x=sym.symbols('x')
f = x*(1-sym.log(x))
xlist=np.linspace(0.5,4,1000)
ylist=sym.lambdify(x,f)(xlist)
plt.plot(xlist,ylist)
plt.plot(1.471517764,f.subs(x,1.471517764),marker="o",markeredgecolor="red",markerfacecolor="green")
plt.text(1.471517764,f.subs(x,1.471517764),'P')
plt.show()

