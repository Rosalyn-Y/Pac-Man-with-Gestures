import cv2 
import numpy as np
import copy
import math
import os

#parameters
cap_x=0.5  # start point/total width
cap_y=0.8  # start point/total height
threshold = 60  #  Binary threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50
learningRate = 0
Bg_flag = 1
Count_flag = True
point_temp = 0

# 1. skin detection & remove background
def SkinMask(img):
    YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) #convert to YCrCb space
    (y,cr,cb) = cv2.split(YCrCb) #split Y, Cr, Cb value
    cr1 = cv2.GaussianBlur(cr, (5,5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Ostu process
    res = cv2.bitwise_and(img,img, mask = skin)
    res = res[0:int(cap_y * img.shape[0]),
                   int(cap_x * img.shape[1]):img.shape[1]]  # clip the ROI
    #cv2.imshow('SkinMask', res)
    return res

#2.Morphology: Dilation & Erosion
def Morph(res):
    kernel = np.ones((8,8), np.uint8) #set kernel size (testing...)
    erosion = cv2.erode(res, kernel) #erosion
    #cv2.imshow("erosion",erosion)
    dilation = cv2.dilate(erosion, kernel)#dilation
    #cv2.imshow("Morphology",dilation)
    return erosion

 # 3.Convert the image into binary image
def th(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
    #cv2.imshow('blur', blur)
    ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('threshold', thresh)
    return thresh

# Calculate the points between fingers
def calculateFingers(res,drawing):
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull) #return coordinates
        if type(defects) != type(None):  # avoid crashing

            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # if the angle is less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.line(drawing, far, start, [211, 200, 200], 2)
                    cv2.line(drawing, far, end, [211, 200, 200], 2)
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0


#open camera
videoCap = cv2.VideoCapture(0)

if (not videoCap.isOpened()):
    print("error: can't find pi camera")
#else:
	#print("success : pi camera is open")


while videoCap.isOpened():
    ret, frame = videoCap.read()

    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    #cv2.imshow('original', frame)
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    cv2.rectangle(frame, (int(cap_x * frame.shape[1]), 0),
                 (frame.shape[1], int(cap_y * frame.shape[0])), (255, 0, 0), 2)#drawing ROI
    cv2.imshow('originalflip', frame)

    if Bg_flag == 1:
        img = SkinMask(frame)#skin detection
        img = Morph(img) #optimize the image, modify in morphology
        thresh = th(img)# convert the image into binary image

        # get the contours
        thresh1 = copy.deepcopy(thresh)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        #print(length)
        maxArea = -1
        if length > 0:
            for i in range(length):  # find the biggest contour (according to area)
                temp = contours[i]
                area = cv2.contourArea(temp)
                if area > maxArea:
                    maxArea = area
                    maxi = i

            res = contours[maxi]
            #print(res)
            hull = cv2.convexHull(res)
            drawing = np.zeros(img.shape, np.uint8)
            cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
            cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

            isFinishCal,cnt = calculateFingers(res,drawing)
            if Count_flag is True:
                if isFinishCal is True:
                    if point_temp != cnt:#when gesture changes, create direction commands
                            #print ("points:", cnt)
                            
                        if cnt == 4:
                            os.system("touch left.txt")
                        elif cnt == 3:
                            os.system("touch right.txt")
                        elif cnt == 1:
                            os.system("touch up.txt")
                        elif cnt == 2:
                            os.system("touch down.txt")
                            
                    point_temp = cnt

        cv2.imshow('output', drawing) # show contours & points in a live screen


    # Keyboard Control
    k = cv2.waitKey(10)
    if k == 27:  # press ESC to exit
        videoCap.release()
        cv2.destroyAllWindows()
        break
    # the followings are used in debug
    elif k == ord('a'): # press a, begin image processing
        Bg_flag = 1
        print( 'Begin image processing')
    elif k == ord('c'): #press c, begin calculation
        Count_flag = True
        print ('Counting')

