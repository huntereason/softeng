import sys
import unittest
import convert
from convert import *

class ConvertTests(unittest.TestCase):
	def test1(self):
		self.assertEqual(convert.readCSV('Student.csv'),[['StudentID', 'FirstName', 'LastName'], ['970100', 'Tom', 'Smith'], ['970101', 'David', 'Washington']])










if __name__ == '__main__':
	unittest.main()
	print "Testing is complete."
