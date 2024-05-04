import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        print('About to run a test')

    # Tests expected value under a normal parameter passed
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(15, result)

    # Tests when a string, or NAN, is passed to func
    def test_do_stuff_errors(self):
        test_param = 'asafaf'
        result = main.do_stuff(test_param)
        # If we return an error, it's actually an instance of an error so we have to do:
        # self.assertEqual(result, ValueError) 

        # This tests whether result is an instance of a ValueError
        self.assertIsInstance(result, ValueError)
    
    # Test when None is passed to the func
    def test_do_stuff2(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff3(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self) -> None:
        print('Cleaning up')
        
if __name__ == '__main__':
    # This will run the entire test file
    unittest.main()