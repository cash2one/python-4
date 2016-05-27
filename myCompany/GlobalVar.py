from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver  = webdriver.Chrome();
wait = WebDriverWait(driver,30);