import time
import datetime

def wait(a, run_num):
    run_num = datetime.datetime.now()
    print(a, "     ", run_num)
    time.sleep(60)