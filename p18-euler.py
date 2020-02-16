# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:16:13 2019

@author: kisch
"""

from triangle_maximum import TriangleMaximum as TM


problem_number = 18


print("Calculation started")


tm = TM()
tm.import_triangle("the_triangle.txt")


for i in range(7,5,-1):
    print(i)

the_answer = 0


print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)


