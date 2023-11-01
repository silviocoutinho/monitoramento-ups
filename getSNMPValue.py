from pysnmp.entity.rfc3413.oneliner import cmdgen
import os, time
from dotenv import load_dotenv
load_dotenv()

start = time.time()

SNMP_HOST = os.getenv("SNMP_HOST")
SNMP_PORT = os.getenv("SNMP_PORT")
SNMP_COMMUNITY = os.getenv("SNMP_COMMUNITY")

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