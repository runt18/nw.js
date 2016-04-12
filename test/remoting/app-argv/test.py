import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
driver.implicitly_wait(5)
time.sleep(1)
try:
    print driver.current_url
    result = driver.find_element_by_id('result-argv').get_attribute('innerHTML')
    print 'nw.App.argv = {0!s}'.format(result)
    assert('nwapp=' not in result)
    result = driver.find_element_by_id('result-fullargv').get_attribute('innerHTML')
    print 'nw.App.fullArgv = {0!s}'.format(result)
    assert('nwapp=' in result)
finally:
    driver.quit()
