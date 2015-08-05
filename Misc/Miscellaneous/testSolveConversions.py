__author__ = 'a-aron'
import unittest
import solveConversions

class test_solve_conversions(unittest.TestCase):

    def test_name_not_taken(self):
        file_that_exists = "testSolveConversions.py"
        attribute_that_doesnt_exist = "something_that_doesnt_exist"
        self.assertTrue(solveConversions.name_not_taken(file_that_exists, attribute_that_doesnt_exist))

    def test_name_is_taken(self):
        file_that_exists = "testSolveConversions.py"
        attribute_that_doesnt_exist = "something_that_doesnt_exist"
        self.assertFalse(solveConversions.name_is_taken(file_that_exists, attribute_that_doesnt_exist))

    def test_convert_into_base_units(self):

        self.assertEquals(solveConversions.convert_into_base_units(['hour', 'hour', 12960, 'kg', 'kilometer']), ['second', 'second', 1.0, 'kilogram', 'meter'])

if __name__ == "__main__":
    unittest.main()