import cv2
from pyagender import PyAgender
from fer import FER

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #classifier
img = cv2.imread("/Extracted_Image/sample22.jpg")   #gets the image as input
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #grayscale image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)


# displaying rectangle
for x, y, w, h in faces[:2]:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

count = 0
for x in list(faces[:2]):
    agender = PyAgender()
    faces = agender.detect_genders_ages(img)
    gender = faces[count]['gender']
    count = count + 1
    print(gender)
    age = int(faces[0]['age'])
    if (gender < 0.5):
        print('G_Male')
    else:
        print('G_Female')
    print('age =', age)
    detector = FER()
    result = detector.top_emotion(img)
    print('Emotion :', result[0])

cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()