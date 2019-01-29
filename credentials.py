import random
import string

class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)

	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass
