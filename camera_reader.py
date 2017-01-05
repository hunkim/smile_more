# http://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python
# export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
# http://stackoverflow.com/questions/28566972/why-are-webcam-images-taken-with-python-so-dark

import cv2
import settings
import math

# https://gist.github.com/46bit/d49f6fd44b9e690a6ac5
def cascade_detect(image):
    distance = 0.0
    font = cv2.FONT_HERSHEY_SIMPLEX

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces =  cascade.detectMultiScale(
        gray_image,
        scaleFactor = 1.2, # change it to a small number to detect more
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Add squeres for each face
    for (x, y, w, h) in faces:
        distancei = (2 * 3.14 * 180) / (w + h * 360) * 1000 + 3
        distance = distancei * 2.54
        distance = math.floor(distance)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray_image[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.putText(image, 'Distance = ' + str(distance), (5, 100), font, 1, (255, 255, 255), 2)
    return faces, distance


'''
Save image and return distance
'''
def make_picture():
    ramp_frames = 30
    camera = cv2.VideoCapture(settings.CAMERA_PORT)

    for i in xrange(ramp_frames):
        s, camera_capture = camera.read()
        if not s:
            return -1 # camera error

    cv2.imwrite(settings.IMG_NAME, camera_capture)
    faces, distance = cascade_detect(camera_capture)
    cv2.imwrite(".det" + settings.IMG_NAME, camera_capture)

    if len(faces) >= 1:
        return distance # OK

    return 0 # no face

if __name__ == '__main__':
    dist = make_picture()
    if dist > 0:
        print ("check image", settings.IMG_NAME, " distance: ", dist)
    else:
        print ("check camera setting and index")

