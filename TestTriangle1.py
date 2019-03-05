# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRta(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRtb(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRtc(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')
        
    def testEquil(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    
    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 7, 8), "Scalene", "4,7,8 should be scalene triangle")

    def testIso1(self):
        self.assertEqual(classifyTriangle(4, 4, 6), 'Isoceles', '4,4,6 should be a isoceles triangle')

    def testIso2(self):
        self.assertEqual(classifyTriangle(4, 6, 4), 'Isoceles', '4,6,4 should be a isoceles triangle')

    def testIsoc3(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isoceles', '6,6,4 should be a isoceles triangle')

    def testNot1(self):
        self.assertEqual(classifyTriangle(2, 2, 4), 'NotATriangle', '2,2,4 should not be a triangle')

    def testNot2(self):
        self.assertEqual(classifyTriangle(4, 2, 2), 'NotATriangle', '4,2,2 should not be a triangle')

    def testNot3(self):
        self.assertEqual(classifyTriangle(2, 4, 2), 'NotATriangle', '2,4,2 should not be a triangle')

    def testinput1(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput', "200,10,10 should be invalidinput")

    def testinput2(self):
        self.assertEqual(classifyTriangle(20, 201, 20), 'InvalidInput', '20,200,20 should be invalidinput')

    def testinput3(self):
        self.assertEqual(classifyTriangle(10, 10, 201), 'InvalidInput','10,10,201 should be invalidinput')

    def testinput4(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be invalidinput')

    def testinput5(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1,1,0 should be invalidinput')

    def testinput6(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1,0,1 should be invalidinput')   

    def testinput7(self):
        self.assertEqual(classifyTriangle("a", 1, 2), 'InvalidInput', 'a,1,2 should be invalidinput')

    def testinput8(self):
        self.assertEqual(classifyTriangle(1, 2.5379, 2), 'InvalidInput', '2,2.5379,2 should be invalidinput')

    def testinput9(self):
        self.assertEqual(classifyTriangle(1, 2, 'a'), 'InvalidInput', '1,2,a should be invalidinput')
    

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


