from time import sleep
from selenium import webdriver
import sys


def test_scores_service(URL):
    driver = webdriver.Chrome(executable_path="tests/chromedriver.exe")
    driver.get(URL)
    sleep(1)
    text = driver.find_element_by_id("score").text
    if int(text) >=0 and int(text) <= 100 :
        driver.close()
        return True
    else :
        driver.close()
        return False

def main_function():
    score = test_scores_service("http://127.0.0.1:5000/")
    if  (score)== True :
        print("Sucess: ")
        sys.exit(0)
    else :
        print("Failure")
        sys.exit(-1)


main_function()