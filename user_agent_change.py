from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

nt = random.randint(25,52)
def func(num):
    while True:
        ua = (f"Mozilla/5.0 (Windows NT {num}; Win64; x64) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/120.0.0.0 Safari/537.36")

        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-agent={ua}")

        driver = webdriver.Chrome(options=options)
        driver.get("https://whatmyuseragent.com/")

        ua_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )
        print(f"Задали: {ua}")
        print(f"Сайт видит: {ua_element.text}")

        input("Нажмите Enter для выхода...")
        driver.get("https://whatmyuseragent.com/")

func(nt)