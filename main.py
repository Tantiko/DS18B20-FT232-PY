import serial
import cv2

COM='COM6' #your com-port with FT232

def s_hello():
    ser = serial.Serial(COM, 9600)
    ser.write(b'\xf0')                  # write a string
    x = ser.read()                      # read answer
    if x == b'\xe0':
        r=0
        #print("successful reset")
    elif x == b'\xf0':
        print("Connection error")
    else:
        print("unknown answer")
    ser.close()

def chek_temp():
    ser = serial.Serial(COM, 115200)
    r = b'\x00\x00\xFF\xFF\x00\x00\xFF\xFF\x00\x00\xFF\x00\x00\x00\xFF\x00' #8 bits address + 8 bits command
    ser.write(r)
    s = ser.read(16)    #clear buf
    ser.close()

def give_temp():
    ser = serial.Serial(COM, 115200)
    r = b'\x00\x00\xFF\xFF\x00\x00\xFF\xFF\x00\xFF\xFF\xFF\xFF\xFF\x00\xFF' #8 bits address + 8 bits command
    b = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF' #template for an answer
    ser.write(r)
    s = ser.read(16)    #clear buf
    ser.write(b)
    i=0
    tt='' #decoding of the answer as a string
    while i < 16:
        i = i + 1
        s = ser.read()
        if s == b'\xFF':
            tt='1'+tt
        else:
            tt='0'+tt
    bin_tt=int(tt,2)        #Bin string to int
    print(bin_tt*0.0625)    #normalization and print
    ser.close()
    
while 1==1:
    s_hello()
    chek_temp()
    s_hello()
    give_temp()
    key = cv2.waitKey(1000) #wait 1 sec.
