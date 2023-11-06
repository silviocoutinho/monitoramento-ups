
from pysnmp.entity.rfc3413.oneliner import cmdgen
import time, datetime
import os, sys
from dotenv import load_dotenv
load_dotenv()

from getSNMPValue import getSNMPValue

SNMP_OID_UPS = os.getenv("SNMP_OID_UPS")
SECONDS_TO_TIMESTAMP = os.getenv("SECONDS_TO_TIMESTAMP")
WAIT_TIME_TO_SHUTDOWN = os.getenv("WAIT_TIME_TO_SHUTDOWN")

# Parametro monitorado
# UPS-MIB::upsInputVoltage.1.0 = INTEGER: 210 RMS Volts
# 1.3.6.1.2.1.33.1.5.3.1.2.1.0 = INTEGER: 240

def sendMessage(msg):
    print('OK ', msg)


def monitor(timeStamp):
    
    time.sleep(5)   
    timeStamp = timeStamp + 5
    
    if (timeStamp > SECONDS_TO_TIMESTAMP):
        timeStamp = 0
        ct = datetime.datetime.now()
        print("current time:-", ct)

    voltagem = getSNMPValue(SNMP_OID_UPS)

    if (voltagem == "0"):
        time.sleep(WAIT_TIME_TO_SHUTDOWN) # 15min
        voltagem = getSNMPValue(SNMP_OID_UPS)
        if (voltagem == "0"):
            sendMessage('desligar')
            sys.exit(0)
    
    return  timeStamp


timeStamp = 0  
while True:    
    timeStamp = monitor(timeStamp)
   


