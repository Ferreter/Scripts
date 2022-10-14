from selenium import webdriver

#This defines the FirefoxProfile where fp=FirefoxProfile stores it
fp= webdriver.FirefoxProfile('/home/ferreter/.mozilla/firefox/rzcvp3g8.default')
driver = webdriver.Firefox(fp)

def main_activity(url,css_selector):
    driver.get(url)
    button_element = driver.find_element_by_css_selector()
    button_element.click()
    driver.quit

main_activity('http://csgobounty.com/#/rewards','div.medium-1:nth-child(2) > a:nth-child(1)')
