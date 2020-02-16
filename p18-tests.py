# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:08 2019

@author: kisch
"""

import unittest

from triangle_maximum import TriangleMaximum as TM


class TestTriangleMaximum(unittest.TestCase):
    
    def setUp(self):
        self.tm = TM()
        self.tm.import_triangle("test_triangle.txt")

        
    def test_import_triangle_data(self):
        ex = [[3],
              [7,4],
              [2,4,6],
              [8,5,9,3]]
        

        self.assertEqual(ex, self.tm.__tr_data__)
        
    def test_find_triagnle_maximum(self):        
        ex = 23
        self.assertEqual(ex, self.tm.find_triangle_maximum())
    




if __name__ == '__main__':
    unittest.main(verbosity=0)
