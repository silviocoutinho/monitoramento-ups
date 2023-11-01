
from pysnmp.entity.rfc3413.oneliner import cmdgen
import time, datetime
import os, sys

from getSNMPValue import getSNMPValue



# Parametro monitorado
# UPS-MIB::upsInputVoltage.1.0 = INTEGER: 210 RMS Volts
# 1.3.6.1.2.1.33.1.5.3.1.2.1.0 = INTEGER: 240

def sendMessage(msg):
    print('OK ', msg)


def monitor(timeStamp):
    
    time.sleep(5)   
    timeStamp = timeStamp + 5
    
    if (timeStamp > 360):
        timeStamp = 0
        ct = datetime.datetime.now()
        print("current time:-", ct)

    voltagem = getSNMPValue('1.3.6.1.2.1.33.1.3.3.1.3.1.0')

    if (voltagem == "0"):
        time.sleep(90) # 15min
        voltagem = getSNMPValue('1.3.6.1.2.1.33.1.3.3.1.3.1.0')
        if (voltagem == "0"):
            sendMessage('desligar')
            sys.exit(0)
    
    return  timeStamp


timeStamp = 0  
while True:    
    timeStamp = monitor(timeStamp)
   


