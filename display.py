import time
import globals
from RPLCD.i2c import CharLCD
from datetime import date, datetime

lcd = CharLCD(i2c_expander='PCF8574', address=0x3f, port=1,
        cols=20, dotsize=8,
        charmap='A02',
        auto_linebreaks=True,
        backlight_enabled=True)
def show_time():
    lcd.write_string(datetime.now().strftime('%Y/%m/%d  %H:%M:%S'))
    lcd.cursor_pos = (1,0)
    lcd.write_string(datetime.today().strftime('%A'))

def display_plzpressbutton():
    lcd.clear()
    lcd.write_string('FAIL !')
    lcd.cursor_pos= (1,0)
    lcd.write_string('please PRESS BUTTON')
    lcd.cursor_pos= (2,0)
    lcd.write_string('before you scan card.')
    time.sleep(1)
def display_registered():
    lcd.clear()
    # ID_number = upload.ID_number
    print(globals.ID_number)
    lcd.write_string('Welcome! ')
    lcd.write_string(globals.ID_number)
    time.sleep(1)
    
def display_default():
    # print(globals.state)
    if globals.state != 'default':
        lcd.clear()
        globals.state = 'default'
        show_time()
        lcd.crlf()
        lcd.write_string('Press and scan')
    else:
        lcd.cursor_pos = (0,0)
        show_time()    
        
        
def display_unregistered():
    lcd.clear()
    lcd.write_string('Unregistered!\n\rPlease contact the \n\radmin')
    time.sleep(1)

    
#default: 時間:先按按鈕 再刷卡 
#刷完:  1. 學號 歡迎
#       2.(fail) you haven't register, plz contact to the  admin
