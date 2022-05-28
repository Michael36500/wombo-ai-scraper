import os
import threading
import time
from cv2 import imwrite
import requests
from io import BytesIO
# import cv2

# import crop_img as crop

#Import third part modules
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#YOU NEED TO SET THE CHROME DRIVER PATH
CHROME_DRIVER_PATH = "c:/Users/ambro/webdrivers/chromedriver.exe"

#XPATH FOR FINDING ELEMENTS ON THE PAGE

XPATH_TEXT_FIELD = "/html/body/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input"
XPATH_IMG_TYPE = '//img[@class="Thumbnail__StyledThumbnail-sc-p7nt3c-0 gVABqX"'
XPATH_BTN_GENERATE = "/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/button"
XPATH_RESULT_IMG = '/html/body/div[1]/div/div[3]/div/div/div[2]/div/img'

XPATH_NAME_TEXT = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/input'
XPATH_SAVE = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[4]/div[1]/button'
#Category of images to generate
CATEGORIES = ["Mystical"]
# CATEGORIES = ["Mystical","HD","Synthwave","Vibrant"]

#This is all current categories on wombo.art
#CATEGORIES = ["Etching","Baroque","Mystical","Festive","Dark Fantasy","Psychic","Pastel","HD","Vibrant","Fantasy Art","Steampunk","Ukiyoe","Synthwave","No Style"]

def downloadImage(imgType,inputText,iteration):

    #Add headless option
    browserOptions = Options()
    #browserOptions.add_argument("--headless")

    #Create driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=browserOptions)
    driver.get("https://app.wombo.art/")

    #Type the text
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH ,XPATH_TEXT_FIELD)))
    textfield.send_keys(inputText)

    #Select the img type to generate
    imgTypeBox = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f'{XPATH_IMG_TYPE} and @alt="{imgType}"]')))
    imgTypeBox.click()

    time.sleep(1)

    #Click on the "Create" button
    btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_BTN_GENERATE)))
    btnGenerate.click()

    #Type the text
    textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH ,XPATH_NAME_TEXT)))
    textfield.send_keys(inputText)

    #Click on the "Save" button
    btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_SAVE)))
    btnGenerate.click()
    
    time.sleep(10)
    


    #Get the generated image
    # resultImg = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,XPATH_RESULT_IMG)))
    # time.sleep(1)
    # resultImgSrc = resultImg.get_attribute('src')

    # time.sleep(5)

    #Get the image from URL
    # im = Image.open(BytesIO(requests.get(resultImgSrc).content))
    # print(im)
    #Crop the image to remove the "Watermark"
    # im = im.crop((65, 165, 950, 1510))
    #Save image localy
    # im.save(f"{inputText}/{str(iteration)+inputText+imgType}.png")
    # img = cv2.imread(f"{inputText}/{str(iteration)+inputText+imgType}.png")
    # img = cv2.pyrUp(img)
    # cv2.imwrite((f"{inputText}/{str(iteration)+inputText+imgType}.png"), img)


#List of driver threads
driverThreads = []

# inputText = input("What do you want to generate with AI : ")
inputText = "Space"
inputText = "".join([x.capitalize() for x in inputText.split(" ")])
# iterations = int(input("Number of iterations : "))
iterations = 5

#Create directory
if not os.path.exists(inputText):
    os.mkdir(inputText)

for i in CATEGORIES:
    for j in range(iterations):
        #Add thread to the list
        driverThreads.append(threading.Thread(target=downloadImage, kwargs={'imgType':i.replace(" ",""),'inputText':inputText,'iteration':j}))

#Start all threads
for i in driverThreads:
    try:
        imgType = i._kwargs.get("imgType")
        iteration = i._kwargs.get("iteration")+1
        print(f"Starting Thread, Type {imgType}, Iteration {iteration}")
        i.start()
    except:
        pass

#Wait for the end of all threads
for i in driverThreads:
    i.join()


# crop.crop()