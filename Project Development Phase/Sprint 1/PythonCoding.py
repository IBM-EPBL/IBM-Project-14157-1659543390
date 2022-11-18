import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization = "mfy87c"
deviceType = "device3"
deviceId = "1357"
authMethod = "token"
authToken = "12345678"

def myCommandCallback(cmd):
    print("Command recieved : %s"% cmd.data['command'])
    status = cmd.data['command']
    if status == "lighton":
        print("LED is on")
    else:
        print("LED is Off")

try:
        deviceOptions = {"org": organization ,  "type": deviceType,"id":deviceId,"auth-method":authMethod,"auth-token":authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)

except Exception as e:
        print("Caught exception connecting device: %s"%str(e))
        sys.exit()

deviceCli.connect()
while True:
    for i in range(10):
        
        Bin1Level= random.randint(0,100)
        Bin2Level = random.randint(0,100)
        Bin3Level = random.randint(0,100)

        data1={'Bin1Level':Bin1Level ,'Bin2Level':Bin2Level,'Bin3Level':Bin3Level}

        if Bin1Level > 90:
            warn1 = 'alert bin full'
        elif Bin1Level > 60:
            warn1 = 'Time to clean'
        else:
            warn1= 'May be cleaned later'

        if Bin2Level > 90:
            warn2 = 'alert bin full'
        elif Bin2Level > 60:
            warn2 = 'Time to clean'
        else:
            warn2= 'May be cleaned later'

        if Bin3Level > 90:
            warn3= 'alert bin full'
        elif Bin3Level > 60:
            warn3= 'Time to clean'
        else:
            warn3= 'May be cleaned later'

        def myOnPublishCallback():
            print("\nPublished Bin1Level = %s "%Bin1Level,
                  "Bin2Level = %s "%Bin2Level ,
                  "Bin3Level = %s "%Bin3Level,"to IBM Watson")
            print("Bin1-%s"%warn1)
            print("Bin2-%s"%warn2)
            print("Bin3-%s"%warn3)
        success = deviceCli.publishEvent("IoTSensor","json",data1,qos=0,on_publish=myOnPublishCallback)
        if not success:
            print("Not cnncted to IOTF")
        time.sleep(10)
        deviceCli.commandCallback=myCommandCallback
deviceCli.disconnect()
        
