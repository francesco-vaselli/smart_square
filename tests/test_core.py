# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:29:38 2020

@author: Francesco
"""

import unittest

from smartsquare.core import square

class TestCore(unittest.TestCase):
    '''
    Unittest for core module
    '''
    def test_float(self):
        '''
        test with floats
        '''
        self.assertAlmostEqual(square(2.), 4)

if __name__ == '__main__':
    unittest.main()
     