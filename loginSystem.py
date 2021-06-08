#!/usr/bin/python3at /etc/os-release
import serial
import time
import globals
from upload import uploadtoGsheet
from display import display_registered, display_default, display_unregistered, display_plzpressbutton

purposeList = [
    "MKS管理",
    "討論/讀書/來坐坐",
    "零星使用",
    "物品寄放",
    "部課/沙龍/部聚",
    "其他",
    "課程/專題",
    "比賽",
    "校務",
    "系上活動",
    "學術部",
    "個人/其他"
]

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        UID = line[:8]
        purpose = line[9:]
        purpose = purpose.split(" ")
        #print(purpose)
        if line != "":
            if purpose == ['']:
                globals.state = "missing button"
                display_plzpressbutton()
                continue
            ser.write(b"Hello from Raspberry Pi!\n")
            print("UID is :", UID)
            for i in range (len(purpose)):
                # print(type(purpose[i]))
                print(purposeList[int(purpose[i])])
                #end of receiving from mega, start to upload to Gsheet
                uploadtoGsheet(UID,purposeList[int(purpose[i])])
            #end of upload to Gsheet,begin to display on the screen
            if globals.state == 'registered':
                display_registered()
            else:
                display_unregistered()
        #elif line != "":
        #    globals.state = 'missing button'
        #    display_default()
        else:
            display_default()

