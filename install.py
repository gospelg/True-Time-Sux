from cryptography.fernet import Fernet
from subprocess import call
import os
import ConfigParser

def create_config(user, password, cwd):
    webiste = 'https://unionskyward.nefec.org:444/scripts/wsisa.dll/WService=wsFin/seplog01.w'
	filepath = cwd + 'setup.ini'
    if os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            Config.set('GENERAL', 'password', password)
	else:    
        with open(filepath, 'w') as f:
	        Config.add_section('GENERAl')
		    Config.set('GENERAL', 'driver', '{0}chromedriver.exe'.format(cwd))
            Config.set('GENERAL', 'website', website)		
            Config.set('GENERAL', 'user', user)
		    Config.set('GENERAL', 'password', password)
		    Config.write(f)
        
def main():
    cwd = os.getcwd()
    key = '' #insert encryption key here. Should match the key in the code of main file.
    cipher_suite = Fernet(key)
	username = input('What is your Skyward login username?\n')
	password = input('What is your password?\n')
	password_encrypt = cipher_suite.encrypt(password)
	
	try:
	    create_config(user, password, cwd)
	except:
	    print 'Failed to create config file.'
	
main()

