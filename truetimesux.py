from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cryptography.fernet import Fernet
import sys
from time import sleep
import ConfigParser

def punch(driver_path, website, user, password, clockin):
    if clockin == True:
        punch_elem = '//*[@id="IN"]'
    else:
        punch_elem = '//*[@id="GONE"]'
    driver = webdriver.Chrome(driver_path, port=444)
    driver.get(website)
    sleep(1)
    sequence = [user, Keys.TAB, password, Keys.RETURN]
    element = driver.find_element_by_xpath('//*[@id="login"]')
    element.send_keys(sequence)
    element.clear
    sleep(1)
    #switch to logged in pop-up window...
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)
    element = driver.find_element_by_xpath('//*[@id="link_trueTime"]')
    element.click()
    sleep(1)
    #switch to third freaking pop up...
    new_window2 = driver.window_handles[2]
    driver.switch_to_window(new_window2)
    element = driver.find_element_by_xpath(punch_elem)
    element.click()
    sleep(1)
    #close windows
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
        driver.close()
    driver.quit()
    
def main():
    try:
        clockin = sys.argv[1]
    except:
        clockin = 'clockout'
    key = '' #cypher key goes here
    cipher_suite = Fernet(key)
    Config = ConfigParser.ConfigParser()
    Config.read('setup.ini')
    driver_path = Config.get('GENERAL', 'driver')
    website = Config.get('GENERAL', 'website')
    user = Config.get('GENERAL', 'user')
    password = cipher_suite.decrypt(Config.get('GENERAL', 'password'))
    
    if clockin == '-clockin':
        punch(driver_path, website, user, password, True)
    else:
        punch(driver_path, website, user, password, False)  
    
main()
