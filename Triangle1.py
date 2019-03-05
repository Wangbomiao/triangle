# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
def classifyTriangle(a, b, c):
    try:
        if isinstance(b, int) and isinstance(a, int) and isinstance(c, int):
            next
        else:
            return 'InvalidInput'
    except ValueError:
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    elif a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type  
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if a+b <= c or b+c <= a or a+c <= b:
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a and a == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c) or ((c*c)+(b*b)) == (a*a) or ((c*c)+(a*a)) == (b*b):
        return 'Right'
    elif (a == b) or  (b == c) or (a == c):
        return 'Isoceles'

    return 'Scalene'
