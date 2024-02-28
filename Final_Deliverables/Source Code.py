from geopy.geocoders import Nominatim
import wiotp.sdk.device
import time
import random
myConfig = {
    "identity": {
        "orgId": "x390n3",
        "typeId": "Publish",
        "deviceId":"9442432"
    },
    "auth": {
        "token": "123456789"
    }
}
a=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,40,41,50,55,60,65]
b=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,40,60]

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=round(random.uniform(0,99.99),2)
    g1=random.choice(a)
    g2=random.choice(b)
    f="EMERGENCY"
    h="Alert"
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("kanchipuram")
    getLoc1= loc.geocode("chennai")
    lat=getLoc.latitude
    log=getLoc.longitude
    lat1=getLoc1.latitude
    log1=getLoc1.longitude
   
    myData={'temperature':temp, 'humidity':hum,'gas_1':g1}
    if g1 > 40:
        myData={'alert_gas_1':f,'latitude':lat,'longitude':log,'gas_1':g1}
    else:
        myData={'temperature':temp, 'humidity':hum,'gas_1':g1}
    if g2 > 40:
        myData1={'alert_gas_2':h,'latitude':lat1,'longitude':log1,'gas_2':g2}
    else:
        myData1={'temperature1':temp, 'humidity1':hum,'gas_2':g2}
       
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    client.publishEvent(eventId="status", msgFormat="json", data=myData1, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    print("Published data successfully: %s", myData1)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
