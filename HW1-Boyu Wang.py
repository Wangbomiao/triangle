import unittest
import math
def classify_triangle(a1,b1,c1):
    try:
        a1=float(a1)
        b1=float(b1)
        c1=float(c1)
    except:
        return "you must type numbers"
    n=[a1,b1,c1]
    m=sorted(n)
    a=m[0]
    b=m[1]
    c=m[2]
    if a+b>c:
        if a==b or b==c:
            if a==b==c:
                return "equilateral triangle"
            elif math.sqrt(a*a+b*b)==c:
                return 'right triangle'
            else:
                return 'isoceles triangle'

        else:
            if math.sqrt(a*a+b*b)==c:
                return 'right triangle'
            else:
                return 'scalene triangles'
    else:
        return "the number you give can't form a triangle"

def main():
    '''
    print("please give three sides of the triangle")
    a1=input("a:")
    b1=input('b:')
    c1=input('c:')
    '''
    a1,b1,c1=map(input("please give three sides of the triangle").split())
    answer=classify_triangle(a1,b1,c1)
    print(answer)

'''
if __name__ == '__main__':
    main()
'''

class TriangleTest(unittest.TestCase):
    def testtriangle(self):
        t1=classify_triangle(4,4,4)
        self.assertEqual(t1, "equilateral triangle")
        t2=classify_triangle(4,4,5)
        self.assertEqual(t2,'isoceles triangle')
        t3=classify_triangle(5,3,6)
        self.assertEqual(t3,'scalene triangles')
        t4=classify_triangle(4,3,5)
        self.assertEqual(t4,'right triangle')
        t5=classify_triangle(8,1,2)
        self.assertEqual(t5,"the number you give can't form a triangle")
        t6=classify_triangle(4,4,8)
        self.assertEqual(t6,"the number you give can't form a triangle")
        t7=classify_triangle("a",4,"n")
        self.assertEqual(t7,"you must type numbers")
        t9=classify_triangle(1,1,2**0.5)
        self.assertEqual(t9,'right triangle')
        
    
if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)


