import random
import string

# Global Variables
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)

def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    '''
    Function to generate an 8 character password for a credential
    '''
    gen_pass=''.join(random.choice(char) for _ in range(size))
    return gen_pass
