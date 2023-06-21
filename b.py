import serial
from keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np

def prepare():

    global model, classNames
    np.set_printoptions(suppress=True)
    model = load_model('/home/goeuddeum/pro2/converted_keras/keras_model.h5')
    classNames = open('/home/goeuddeum/pro2/converted_keras/labels.txt','r').readlines()

# ['0 r\n','1 s\n','2 p\n','3 x\n']


def  loop():

    cap = cv2.VideoCapture(0)
    while True:
        ret, image = cap.read()
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imshow("Webcam Image", image)
        
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1
        
        prediction = model.predict(image)
        print('prediction0',prediction)
        index = np.argmax(prediction)
        className = classNames[index]
        # '2 p\n'
        #  0123
        #print('index', index)
        confidenceScore = prediction[0][index]
        print("Class:", className[2:], end="")
        # 'p\n'
        print("Confidence Score:", str(np.round(confidenceScore * 100))[:-2], "%")

        a = className.replace('\n', '')
        if confidenceScore >= 0.5:
            sendMsg(a)
            
        if cv2.waitKey(24) ==27:
            break

    cap.release()

def sendMsg(msg):
    ser.write(msg.encode())


PORT = '/dev/ttyUSB0'
if __name__ == '__main__':

    ser = serial.serial_for_url(PORT, 9600, timeout=1)

    prepare()
    loop()
