# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:10:46 2020

@author: kisch
"""


class TriangleMaximum():
    
    def __init__(self):
        self.__tr_data__ = []
        
    def __add_numbers_to_data(self,nums):
        ind = len(self.__tr_data__)-1
                
        for num in nums:
            if(len(num) > 0):
                self.__tr_data__[ind].append(int(num))
        
    def __read_tr_line__(self,line):
        self.__tr_data__.append([])
        
        if(line[-1] == "\n"):
            line = line[:-1]
            
        nums = line.split(" ")
        self.__add_numbers_to_data(nums)        
        
    
    def import_triangle(self,filename):
        self.__tr_data__ = []
        
        with open(filename,"r") as file:
            lines = file.readlines()
            for line in lines:
                self.__read_tr_line__(line)
                
                
    def __get_next_left__(self,ind,inner_ind):
        
        if(ind >= len(self.__tr_data__)):
            return 0
        
        return self.__tr_data__[ind][inner_ind]
    
    def __get_next_right__(self,ind,inner_ind):
        
        if(ind >= len(self.__tr_data__)):
            return 0
        
        return self.__tr_data__[ind][inner_ind+1]
    
    def find_triangle_maximum(self):
        sum = 0
        sec_i = 0
        
        for i in range(len(self.__tr_data__)):
            sec_i = self.__get_next_inner_ind__(i,sec_i)
            sum += self.__tr_data__[i][sec_i]
            
        
        return sum