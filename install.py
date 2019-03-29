#This file is currently busted, dont use
from cryptography.fernet import Fernet
from subprocess import call
import os
import configparser

def create_config(user, password, cwd):
    Config = configparser.ConfigParser()
    website = 'https://unionskyward.nefec.org:444/scripts/wsisa.dll/WService=wsFin/seplog01.w'
    filepath = cwd + 'setup.ini'
    with open(filepath, 'w') as f:
        Config.add_section('GENERAL')
        Config.set('GENERAL', 'driver', '{0}chromedriver.exe'.format(cwd))
        Config.set('GENERAL', 'website', website)
        Config.set('GENERAL', 'user', user)
        Config.set('GENERAL', 'password', password)
        Config.write(f)

#def create_task(cwd):


def main():
    cwd = os.getcwd()
    key = 'l2GYHWhRkv6rrPgbGGvbAsxQpNo4QF4tNtu1QWEg3uE='
    cipher_suite = Fernet(key)
    username = input('What is your Skyward login username?\n')
    password = input('What is your password?\n')
    password_encrypt = cipher_suite.encrypt(password.encode('ascii'))
    try:
        create_config(username, password, cwd)
    except Exception as ex:
        print('Failed to create config file.')
        print(ex)

main()
