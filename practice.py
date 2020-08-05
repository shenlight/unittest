import unittest
import calculator

class CalcultorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.args = (18,6)

    def test_plus(self):
        expected = 24
        result = calculator.plus(*self.args)
        self.assertEqual(expected,result)
    
    def test_type(self):
        a = "123"
        b = 123
        self.assertIsInstance(a,str) 


def map_lt(mapper, lt):
    result = []
    for ele in lt:
        result.append(mapper(ele))
    return result

sum=0
for i in range(1,5,1):
    for j in range(1,5,1):
        for k in range(1,5,1):
            if(i!=j and j!=k and i!=k):
                sum=sum+1
                print (i,j,k)  # 這裡去重
print(sum)