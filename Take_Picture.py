# Loading Libraries
import picamera
import datetime

def take_picture():
    print("Taking picture...")
    with picamera.PiCamera() as camera:
        #camera.resolution = (1280,720)
        current_time = datetime.datetime.now()
        image_name = "/home/pi/Pictures/" + str(current_time) + ".jpg"
        camera.capture(image_name)
    print("Picture taken.")

take_picture()