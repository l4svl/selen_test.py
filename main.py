from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'lala.txt')
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')
button = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100"))
driver.find_element(By.XPATH, '//*[@id="book"]').click()
x = int(driver.find_element(By.ID, 'input_value').text)
driver.find_element(By.XPATH, '//*[@id="answer"]').send_keys(calc(x))
driver.find_element(By.XPATH, '//*[@id="solve"]').click()
