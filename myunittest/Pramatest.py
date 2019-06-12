# -*- coding: UTF-8 -*-
import unittest,os
from myunittest import testlib
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):

    @parameterized.expand([
        [1,1,2],
        [1.1,1.33333333,2.43333333],


    ])
    def test_add(self,x,y,z):
        """"""
        self.assertEqual(testlib.add(x,y),z)


if __name__ == '__main__':
    unittest.main()
