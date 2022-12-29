import cv2


def findPad(img):
    cascade = cv2.CascadeClassifier("numneg2000/cascade.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(imgGray, 1.2, 8)

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


cap = cv2.VideoCapture("C:/Users/benny/PycharmProjects/cascade/IMG_3979.mov")
#cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    findPad(img)
    cv2.imshow("Output", img)
    cv2.waitKey(1)