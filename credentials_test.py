import unittest
from credentials import Credential


class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('ronney','twitter','buoy','pswd526')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'ronney')
		self.assertEqual(self.new_credential.site_name,'twitter')
		self.assertEqual(self.new_credential.account_name,'buoy')
		self.assertEqual(self.new_credential.password,'pswd526')
	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []


	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credential('ronney','Twitter','buoy','pswd526')
		twitter.save_credentials()
		gmail = Credential('ronney','Gmail','oginga001ronney@gmail.com','pswd200')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name,gmail.user_name)),2)
		self.assertEqual(len(Credential.display_credentials(gmail.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('ronney','Twitter','buoy','pswd526')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)

if __name__ == '__main__':
	unittest.main(verbosity=2)
