# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:16:13 2019

@author: kisch
"""

import numpy as np
import pandas as pd

problem_number = 18


print("Calculation started")

df = pd.read_csv("the_triangle.txt", header=None, sep="\n")
df = df[0].str.split(" ")
df = df.to_numpy()

data = []

for i, li in enumerate(df):
    data.append([])
    for num in li:
        data[i].append(int(num))
        




the_answer = 0



print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)


