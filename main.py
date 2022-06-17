import bot
#import clear as cl
# import womboAiScraper as scrape
import time
import datetime
import os
import womboAiScraper as download
import gn_inp

import wait

# what = os.listdir("Download/")
# print(what)
# cl.clear()

# run_num = 0´d

bot.login()

time.sleep(1)
# while True:



# for a in inputs:
lpnb = 0
while True:
    minute = 24
    while True:
        now = datetime.datetime.now().time()
        if now.minute == minute:
            break
        time.sleep(10)
        print("waiting, going on {}, now is {}, means in {}".format(minute, now.minute, 60 - (now.minute + 60 - minute)))

    files = os.listdir("Download/")
    for file in files:
        os.remove("Download/" + file)
    download.downloadImage("Steampunk","{}".format(gn_inp.gn_inp_short()))
    run_num = datetime.datetime.now()
    # x = time.time()
    # path = "mazes/" + str(x) + ".jpg"y
    # write_p = "write/" + str(run_num) + ".jpg"
    what = os.listdir("Download/")
    path = "Download/" + str(what)
    path = str(path)
    path = path.replace("[", "")
    path = path.replace("]", "")
    path = path.replace("'", "")
    print(path)
    print(path)
    print(path)
    print(path)
    print(path)
    print(path)
    print(path)

    
    # continue
    print(path)
    bot.upload(path)

    lpnb += 1
    path = os.listdir("Download/")
    path = str(path)
    path = path.replace("[", "")
    path = path.replace("]", "")
    path = path.replace("'", "")
    print(path)
    os.remove("Download/" + path)

    # for a in range(60):
    #     wait.wait(a, run_num)