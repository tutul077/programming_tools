# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:52:39 2022
....Compute sum with for loop

"""

# # Problem-1
# x = 0
# n = 10

# for i in range (n+1):
#     #x = x + 5*i
#     x += 5*i
#     print (i, 'of', n, 'x=', x)

# print ('Final value of x after %i iterations ='% n, x)    
# print ('final value of x after %i iterations =%0.2f' %(n,x))    



# # Problem-2 (compute number pi using Leibniz method)
# import numpy
# list = [10,50,100,1000]
# for n in list:
#     sum_pi = 0
#     for k in range (n):
#         sum_pi += 1/((4*k+1)*(4*k+3))
#     sum_pi *=8
    
#     print ('my pi approximation=', sum_pi) 
#     print ('error=', abs (sum_pi-numpy.pi), 'after %i iterations' %(n))   
 


# # Problem-2 (compute number pi using Leibniz method) (using function)
# import numpy
# def my_pi(max_iter):
#     sum_pi = 0
#     for k in range (max_iter):
#         sum_pi += 1/((4*k+1)*(4*k+3))
#     sum_pi *=8
#     print ('my pi approx = ', sum_pi) 
#     print ('error=', abs (sum_pi-numpy.pi), 'after %i iterations'%(max_iter))
#     return ()

# my_pi(100) # Calling function

   
# Problem-3 (Code inC_1_1_ball.py)
# Program for computing the height of a ball in vertical motion

# v0 = 5                # Initial velocity
# g = 9.81              # Acceleration of gravity
# t = 0.6               # Time
# y = v0*t - 0.5*g*t**2 # Vertical position
# print(y)


# Problem-5 (Find the maximum height)

import numpy as np
t = np.linspace(0,2,num=2000)
v0 = 5
g = 9.81

for i in t:
    y = v0*t - 0.5*g*t**2
print('The lagrest y is', max(y))  






























