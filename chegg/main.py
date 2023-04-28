from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



# navigate to the website
driver.get('https://www.google.com')
