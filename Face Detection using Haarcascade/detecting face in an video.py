import cv2 as cv

vid = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier("E:/Extra Codes/Python/Python Programs/OpenCV/Face detection using Haarcascade\haarcascade.xml")
while True:
    a, frame = vid.read()
    flip = cv.flip(frame, 1)
    faces = haar_cascade.detectMultiScale(flip, scaleFactor=1.1, minNeighbors=8)
    for (x,y,w,h) in faces:
        cv.putText(flip, "Vedant", (x,y), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0),2)
        cv.rectangle(flip, (x,y), (x+h,y+w), (0,255,0), thickness=2)
    cv.imshow("video", flip)
    
    if cv.waitKey(1) == ord("q"):
        break
vid.release()
cv.destroyAllWindows()