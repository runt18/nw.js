import time
import os
import subprocess
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nw_util import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def click_and_assert(driver, id, expect):
    driver.find_element_by_id(id).click()
    wait_window_handles(driver, 2)
    print 'switch to opened window'
    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_id('getwinsize').click()
    result = driver.find_element_by_id('result').get_attribute('innerHTML')
    print 'window size: {0!s}'.format(result)
    assert (expect in result)
    driver.close()
    wait_window_handles(driver, 1)
    driver.switch_to_window(driver.window_handles[0])

chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options, service_log_path="log", service_args=["--verbose"])
time.sleep(1)
try:
    print driver.current_url
    driver.implicitly_wait(10)
    print 'open new window with `window.open()`'
    click_and_assert(driver, 'winopen', '800,600')
    print 'open new window with <a target="_blank">'
    click_and_assert(driver, 'winopen', '800,600')
    print 'bind new-win-policy and newly opened window should have size of 488,600'
    driver.find_element_by_id('bindnewwinpolicy').click()
    print 'open new window with `window.open()` after new-win-policy'
    click_and_assert(driver, 'winopen', '488,600')
    print 'open new window with <a target="_blank"> after new-win-policy'
    click_and_assert(driver, 'winopen', '488,600')
finally:
    driver.quit()
