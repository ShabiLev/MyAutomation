# # from unittest import TestCase
# #
# #
# # class Mytest(TestCase):
# #     @classmethod
# #     def setUpClass(clsself):
# #         print('Hello')
# #
# #     def test_02(self):
# #         assert 1 > 3
# #
# #     def test_01(self):
# #         assert 1 > 0
# #
# #     @classmethod
# #     def tearDownClass(cls) -> None:
# #         print('bye bye')
#
# import unittest
#
#
# class TestStringMethods(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("setUpClass")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("tearDownClass")
#
#     def setUp(self):
#         print("setUp")
#
#     def tearDown(self):
#         print("tearDown")
#
#     def test_upper(self):
#         self.assertEqual('hello'.upper(), 'HELLO')
#
#     def test_isupper(self):
#         self.assertTrue('HELLO'.isupper())
#         self.assertFalse('Hello'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# # In this example, we define a test class called TestStringMethods, which inherits from unittest.TestCase.
# # The class includes setUpClass and tearDownClass methods that are called before and after all the tests are run,
# # respectively. It also includes setUp and tearDown methods that are called before and after each individual test,
# # respectively.
# # We then define three different tests: test_upper, test_isupper, and test_split.
# # These tests use various assertion methods provided by the unittest library,
# # such as assertEqual and assertTrue, to check that certain conditions are met.
# # Finally, we use the unittest.main() function to run the tests.
# # When the tests are run, the setUpClass method is called once at the beginning, followed by the setUp method for each test,
# # the three individual tests, the tearDown method for each test, and finally the tearDownClass method once at the end.
# # The output of the script will include the results of the tests as well as any print statements included in the setup and teardown methods.

# import unittest
# import requests as req
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class TestWebPage(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # This method runs once before all tests in the class
#         cls.driver = webdriver.Chrome()
#         cls.driver.get('https://stage2.okoora.com/')
#         cls.driver.maximize_window()
#
#     @classmethod
#     def tearDownClass(cls):
#         # This method runs once after all tests in the class
#         cls.driver.quit()
#
#     def test_click_element(self):
#         # This test clicks an element on the page
#         element = self.driver.find_element(By.CLASS_NAME, 'form-control ng-pristine ng-valid ng-touched')
#
#         element.click()
        # Add any assertions to check that the click worked as expected

    # def test_verify_text(self):
    #     # This test verifies the text of an element on the page
    #     element = self.driver.find_element_by_id("example-element")
    #     expected_text = "Hello, world!"
    #     actual_text = element.text
    #     self.assertEqual(actual_text, expected_text)


# ----------------------------------------------------------------------------------------------------
from unittest import TestCase

class TestStringMethods(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     print("test_split")
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


    def test_words(self):
        words = ['hello', 'beautiful', 'world']
        for word in words:
            assert 'l' in word
        print('Success')


    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


# First, we import the unittest module, which provides a framework for writing and running tests.
# Next, we define a new class called TestStringMethods, which inherits from unittest.TestCase.
# This class contains four methods: setUpClass, setUp, test_upper, test_isupper, test_split, tearDown, and tearDownClass.
# The setUpClass method is a class method that is run once at the beginning of the test suite.
# In this example, it simply prints the message "setUpClass".
# This method can be used to set up any resources that need to be shared across multiple test methods.
#
# The setUp method is an instance method that is run before each individual test method.
# In this example, it simply prints the message "setUp".
# This method can be used to set up any resources that are specific to each test method.
#
# The test_upper, test_isupper, and test_split methods are individual test methods that test specific functionality in the application.
# In this example, each method prints a message indicating which test is being run,
# and uses various assertions to check that the code is working correctly.
#
# The tearDown method is an instance method that is run after each individual test method.
# In this example, it simply prints the message "tearDown". This method can be used to clean up any resources that were created in the setUp method.
#
# The tearDownClass method is a class method that is run once at the end of the test suite.
# In this example, it simply prints the message "tearDownClass".
# This method can be used to clean up any resources that were created in the setUpClass method.
#
# When we run this test using unittest.main(), the output will look something like this:

    # setUpClass

    # setUp
    # test_upper
    # tearDown

    # setUp
    # test_isupper
    # tearDown

    # setUp
    # test_split
    # tearDown

    # tearDownClass
#
# As you can see, the setUpClass and tearDownClass methods are run once at the beginning
# and end of the test suite, respectively. The setUp and tearDown