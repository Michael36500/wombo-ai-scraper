import os
import time
import shutil


from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
 
#YOU NEED TO SET THE CHROME DRIVER PATH
# CATEGORIES = ["Mystical","HD","Synthwave","Vibrant"]

#This is all current categories on wombo.art
# CATEGORIES = ["Etching","Baroque","Mystical","Festive","Dark Fantasy","Psychic","Pastel","HD","Vibrant","Fantasy Art","Steampunk","Ukiyoe","Synthwave","No Style"]


# def delete(path):
#     dele = os.listdir(path)
#     for dlt in dele:
#         print(dlt)
#         dlt = str(path + dlt)
#         os.remove(dlt)
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! jestli chci delete
# delete("Download/")



def downloadImage(imgType,inputText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CHROME_DRIVER_PATH = "{}/chrome_veci/chromedriver_linux64.zip".format(dir_path)   # add your chromedriver path
    print(CHROME_DRIVER_PATH)

    XPATH_GENERETE = "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div[13]/div/div/img"

    browserOptions = webdriver.ChromeOptions()

    browserOptions.add_argument("--head less")

    #Create driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=browserOptions)
    driver.get("instagram.com")


    # #Type the text
    # # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH ,XPATH_TEXT_FIELD)))
    # for a in inputText:
    #     textfield.send_keys(a)
    #     time.sleep(0.1)

    # #Select the img type to generate
    # imgTypeBox = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/img")))
    # imgTypeBox.click()

    # #Click on the "Create" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_GENERETE)))
    # btnGenerate.click()

    # time.sleep(1)


    # #Type the text
    # textfield = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH ,XPATH_NAME_TEXT)))
    # textfield.send_keys(inputText)

    # #Click on the "Save" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_SAVE)))
    # btnGenerate.click()
    
    # time.sleep(10)


downloadImage("XX", "town")