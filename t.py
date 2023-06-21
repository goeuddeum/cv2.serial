import serial
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # COM 9에 115200으로 serial port open

while True:
    print("insert op :")
    op = input()
    ser.write(op.encode())

    rx = ser.readline().decode('ascii')   # 아스키 타입으로 읽음

    print("Receive Data: ", rx)

    if rx == 'q' :  #q가 들어오면 serial comm stop을 print하고 while 문 벗어남
        print('serial comm stop !!!')
        break

ser.close()   # serial 통신 close