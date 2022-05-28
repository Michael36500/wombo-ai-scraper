import os
import cv2

def crop():
    # find every file in Download/ and add them to list
    inputs = os.listdir("Download/")

    for a in inputs:
        print(a)
        # read img
        img = cv2.imread("Download/{}".format(a))

        # crop the img
        crop = img[179 : 1689, 61 : 1018]    


        # write cropped image
        cv2.imwrite("Download/{}".format(a), crop)

crop()