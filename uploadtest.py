import sys
import time
import datetime
import gspread
import json
import signal
from oauth2client.service_account import ServiceAccountCredentials as SAC
from datetime import date, datetime

GDriveJSON = 'pythonupload.json'
GSpreadSheet = 'UploadByPython'
WaitSecond = 5
print('將資料記錄在試算表' ,GSpreadSheet , '每' ,WaitSecond ,'秒')
print('按下 Ctrl-C中斷執行')
count = 1
# testsheet = gc.add_worksheet(title="test sheet", rows="100", cols="20")
while True:
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)

    recordtime = datetime.now()
    worksheet.append_row((recordtime.strftime("%d/%m/%Y %H:%M:%S"), ))
    count = count+1
    print('type sth on the ' ,GSpreadSheet)
    #print(worksheet.cell(count,1).value)
    print(worksheet.row_values(2))
    time.sleep(WaitSecond)










