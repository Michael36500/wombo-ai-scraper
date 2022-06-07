import bot
#import clear as cl
# import womboAiScraper as scrape
import time
import datetime
import os

import wait


#cl.clear()

# run_num = 0´d

bot.login()

time.sleep(1)
# while True:
#     run_num = datetime.datetime.now()
#     # x = time.time()
#     # path = "mazes/" + str(x) + ".jpg"
#     path = "download/" + str(run_num) + ".jpg"
#     write_p = "write/" + str(run_num) + ".jpg"
#     path = str(path)
#     # print(path)


#     # downloadImage(imgType,inputText,iteration):

#     # continue

#     bot.upload(path)

#     for a in range(60):
#         print(a, "     ", run_num)
#         time.sleep(60)


# najde všechny soubory v IN složce, aby se mohl loopnout
inputs_jpg = os.listdir("Download/")
inputs = []
for a in inputs_jpg:
    l = len(a)
    short = a[:l - 4]
    inputs.append(short)
# vynechávám img_num, protože ho nepotřebuji



for a in inputs:
    if "REMOV" in a:
        continue
    run_num = datetime.datetime.now()
    # x = time.time()
    # path = "mazes/" + str(x) + ".jpg"y
    path = "Download/" + str(a) + ".jpg"
    # write_p = "write/" + str(run_num) + ".jpg"
    path = str(path)
    # print(path)


    # downloadImage(imgType,inputText,iteration):
    
    # continue
    print(path)
    bot.upload(path)

    for a in range(60):
        wait.wait(a, run_num)