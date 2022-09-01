from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


elchofer = webdriver.Chrome(r"D:\marioAdair\Universidad\SeptimoSemestre\testing\chromedriver_win32/chromedriver.exe")
elchofer.get("https://www.clima.com/")

elchofer.find_element(By.XPATH, "//a[contains(@href, \'https://www.clima.com/mexico\')]").click()
time.sleep(3)

elchofer.find_element(By.XPATH, "//input[@id=\'term\']").send_keys("Queretaro")
time.sleep(3)

elchofer.find_element(By.XPATH,"//span[contains(text(),'Santa Rosa de Jáuregui, Estado de Querétaro de Art')]").click()
time.sleep(3)

elchofer.find_element(By.XPATH, "//a[contains(text(),\'Por horas\')]").click()
time.sleep(3)

elchofer.find_element(By.XPATH, "//a[contains(text(),\'Días\')]").click()
time.sleep(3)