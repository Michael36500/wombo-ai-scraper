import os
import threading
import time
from cv2 import imwrite
import requests
from io import BytesIO
import shutil


import crop_img as crop

#Import third part modules
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
    CHROME_DRIVER_PATH = "c:/Users/ambro/webdrivers/chromedriver.exe"   # add your chromedriver path

    #XPATH FOR FINDING ELEMENTS ON THE PAGE, maybe you'll need to change them/create a issue

    XPATH_TEXT_FIELD = "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[1]/div[1]/input"
    XPATH_IMG_TYPE = '//img[@class="Thumbnail__StyledThumbnail-sc-p7nt3c-0 gVABqX"'
    XPATH_BTN_GENERATE = "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[3]/div/button"
    XPATH_RESULT_IMG = '/html/body/div[1]/div/div[3]/div/div/div[2]/div/img'

    XPATH_GENERETE = "/html/body/div[1]/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div[13]/div/div/img"

    XPATH_NAME_TEXT = "/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[1]/input"
    XPATH_SAVE = '/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div[4]/div[1]/button'
    #Category of images to generate
    CATEGORIES = ["Steampunk"]
    # imgType = styl obrázku (steampunk, synthwave,...)


    #Add headless option
    browserOptions = Options()
    # browserOptions.add_argument("--headless")

    #Create driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=browserOptions)
    driver.get("https://app.wombo.art/")

    #Type the text
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH ,XPATH_TEXT_FIELD)))
    for a in inputText:
        textfield.send_keys(a)
        time.sleep(0.1)

    #Select the img type to generate
    # imgTypeBox = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f'{XPATH_IMG_TYPE} and @alt="{imgType}"]')))
    # imgTypeBox.click()
    #Click on the "Create" button
    btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_GENERETE)))
    btnGenerate.click()

    time.sleep(1)

    #Click on the "Create" button
    btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_BTN_GENERATE)))
    btnGenerate.click()

    #Type the text
    textfield = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH ,XPATH_NAME_TEXT)))
    textfield.send_keys(inputText)

    #Click on the "Save" button
    btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_SAVE)))
    btnGenerate.click()
    
    time.sleep(10)


    # move images from downloads to Downloads
    path = "c:/Users/ambro/Downloads/"
    files = os.listdir(path)
    for file in files:
        if "TradingCard" in file:
            # shutil.move("c:/Users/ambro/Downloads/{}".format(file), "D:/D/programování/PYTHON/webscrape/wombo-ai-scraper/Download/{}".format(file))
            # change second one into your folder
            shutil.copy("c:/Users/ambro/Downloads/{}".format(file), "D:\D\programování\PYTHON\webscrape\wombo-ai-scraper\Download\{}".format(file))
            print(file)
    #Get the generated image
    crop.crop()
    # resultImg = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,XPATH_RESULT_IMG)))
    print("here")
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
# downloadImage(CATEGORIES[0], "ship")

# #List of driver threads
# driverThreads = []

# # inputText = input("What do you want to generate with AI : ")
# # inputText = "Space"
# # inputText = ["city", "sunset", "sea", "forest", "airship", "port", "robot", "factory", "human", "fly", "waterfall", "tank", "giant robot", "steamtrain", "train"]
# inputText = ["city"]
# # for a in inputText:

# # inputText = "".join([x.capitalize() for x in inputText.split(" ")])
# # iterations = int(input("Number of iterations : "))
# iterations = len(inputText)
# print(iterations)

# #Create directory
# # if not os.path.exists(inputText):
# #     os.mkdir(inputText)

# for a in range(5):
#     for i in CATEGORIES:
#         for j in range(iterations):
#             #Add thread to the list
#             driverThreads.append(threading.Thread(target=downloadImage, kwargs={'imgType':i.replace(" ",""),'inputText':inputText[j],'iteration':j}))

# #Start all threads
# for i in driverThreads:
#     try:
#         imgType = i._kwargs.get("imgType")
#         iteration = i._kwargs.get("iteration")+1
#         print(f"Starting Thread, Type {imgType}, Iteration {iteration}")
#         i.start()
#     except:
#         pass
#     time.sleep(5)

# #Wait for the end of all threads
# for i in driverThreads:
#     i.join()



# crop.crop()
# downloadImage("Steampunk","creepy putin with banana")
