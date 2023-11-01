
from pysnmp.entity.rfc3413.oneliner import cmdgen
import time, datetime
import os, sys
from dotenv import load_dotenv
load_dotenv()

start = time.time()

SNMP_HOST = os.getenv("SNMP_HOST")
SNMP_PORT = os.getenv("SNMP_PORT")
SNMP_COMMUNITY = os.getenv("SNMP_COMMUNITY")

# Parametro monitorado
# UPS-MIB::upsInputVoltage.1.0 = INTEGER: 210 RMS Volts
# 1.3.6.1.2.1.33.1.5.3.1.2.1.0 = INTEGER: 240

def sendMessage(msg):
    print('OK ', msg)

def getSNMPValue(oid):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(SNMP_COMMUNITY),
        cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
        oid
    )
    result = 200
    for name, val in varBinds:
        result = val.prettyPrint()
    return result


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
   


