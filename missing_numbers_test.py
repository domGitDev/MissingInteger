
import unittest
from missing_numbers import find_missing


class FindMissingTest(unittest.TestCase):
	
	def test_missing_pair(self):
		m = 10
		A = [203, 204, 205, 206, 207, 
			208, 203, 204, 205, 206]
		n = 13
		B = [203, 204, 204, 205, 206, 207, 
			205, 208, 203, 206, 205, 206, 204]
			
		self.assertEqual([204, 205, 206], find_missing(A, m, B, n))	
		
	def test_find_missing_type(self):
		with self.assertRaises(TypeError):
			find_missing('dg', 2, [0, 3], 2)
			
		with self.assertRaises(TypeError):
			find_missing(10000, 1, 100, 1)
			
		with self.assertRaises(TypeError):
			find_missing([6, 7, 8], 3, 'this', 4)		

suite = unittest.TestLoader().loadTestsFromTestCase(FindMissingTest)
unittest.TextTestRunner(verbosity=2).run(suite)


