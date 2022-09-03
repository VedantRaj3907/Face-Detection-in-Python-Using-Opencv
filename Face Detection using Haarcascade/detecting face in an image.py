import cv2 as cv

img = cv.imread("E:/Extra Codes/Python/Python Programs/OpenCV/Face Recognition/ronaldo2.jpg",1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("E:/Extra Codes\Python/Python Programs/OpenCV/Face detection using Haarcascade/haarcascade.xml")

faces = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)
#lowering the value of the minneighbors will detect more faces

print("Number of faces :- ", len(faces))

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+h,y+w), (0,255,255), thickness = 3)
    
cv.imshow("face dected", img)



cv.waitKey(0)

cv.destroyAllWindows()