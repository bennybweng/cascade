import cv2

#(imgGray, 1.2, 8)
def findPad(img):
    cascade = cv2.CascadeClassifier("numneg2000/cascade.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pads = cascade.detectMultiScale(imgGray, 1.15, 6)

    for (x, y, w, h) in pads:
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


cap = cv2.VideoCapture("C:/Users/benny/PycharmProjects/cascade/positive_v2/0001_0045_0025_0144_0144_6.jpg")
#cap = cv2.VideoCapture("C:/Users/benny/PycharmProjects/cascade/IMG_3964.mov")
#cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    findPad(img)
    cv2.imshow("Output", img)
    cv2.waitKey(0)