import unittest
from user import User
# import pyperclip

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('ronnie','otieno','pswd100')
		self.new_user.save_user()

		for user in User.users_list:
			if user.first_name == user.first_name and user.password == user.password:
				current_user = user.first_name
		return current_user


	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('ronnie','otieno','pswd100')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'ronnie')
		self.assertEqual(self.new_user.last_name,'otieno')
		self.assertEqual(self.new_user.password,'pswd100')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),2)

@classmethod
def find_by_site_name(cls, site_name):
    '''
    Method that takes in a site_name and returns a credential that matches that site_name.
    '''
    for credential in cls.credentials_list:
        if credential.site_name == site_name:
            return credential
if __name__ == '__main__':
	unittest.main(verbosity=2)
