# ответ на пункт 2.4 8 шаг
import time
from selenium import webdriver
driver = webdriver.Chrome()
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 


driver.get("http://suninjuly.github.io/explicit_wait2.html")
button = driver.find_element_by_id("book")
WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),'100')
)
button.click()	
	


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x = driver.find_element_by_id("input_value").text

y = calc(x)  
input = driver.find_element_by_id("answer")
input.send_keys(str(y))
button2 = driver.find_element_by_id("solve")
button2.click()

time.sleep(5)
driver.quit()
# запускать py C:\Users\allge\Desktop\selenium_course\less216.py