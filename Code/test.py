from selenium import webdriver 

PATH = '/media/omar/Backup/projects/Selenium_tutorial/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()