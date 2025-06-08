from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

url = "https://www.ranker.com/crowdranked-list/the-greatest-rappers-of-all-time"

def fetchNamesFromRanker(url):
    driver = webdriver.Chrome()
    driver.get(url)

    #scroll down the website to the bottom to show all the rappers
    body = driver.find_element(By.TAG_NAME,"body")
    no_of_pagedowns = 100
    sleep_time = random.uniform(0.2, 2)

    while no_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(sleep_time)
        no_of_pagedowns-=1

    web_items = driver.find_elements(By.CLASS_NAME, "NodeName_nameWrapper__zuF49")

    names = []
    for item in web_items:
        names.append(item.text)
    
    with open("rapper_names.txt", "w") as f:
        for name in names:
            f.write(f"{name}\n")
    return names


def readNamesFromLocal(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    return lines
