import sys
import time
import datetime
import gspread
import json
import signal
import globals
from oauth2client.service_account import ServiceAccountCredentials as SAC
from datetime import date, datetime
def uploadtoGsheet(UID,purpose):
    GDriveJSON = '/home/pi/LoginSystem/pythonupload.json'
    GSpreadSheet = 'UserRegister'

    try:
        scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1) 
    try: #if the uid hasn't been recorded
        cell = worksheet.find(UID)
        globals.ID_number = worksheet.cell(cell.row, 4).value
        globals.name = worksheet.cell(cell.row, 3).value
    except:
        globals.ID_number = ""
        globals.name = ""
    
    recordtime = datetime.now()
    worksheet.append_row((recordtime.strftime("%d/%m/%Y"), 
        recordtime.strftime("%H:%M:%S"),globals.name, globals.ID_number,purpose,"",UID))
    
    if globals.ID_number == "" or globals.name == "" or purpose == "":
        globals.state = 'unregistered'
    
    else:
        globals.state = 'registered'
        
        
    






