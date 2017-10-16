# Lucas Childers
# 2017

import requests
import json

# TODO
# Add other methods for API endpoints (https://api.developer.lifx.com/docs)
# Easier way to set color and temperature
# Unit Testing
# PiPy

class easyLIFX:
    class Light:
        def __init__(self, lightId, label, power, brightness):
            self.id = lightId
            self.label = label
            self.power = power
            self.brightness = brightness

        def printInfo(self):
            print("     Name:", self.label,
                "\n       ID:", self.id,
                "\n    State:", self.power,
                "\nBrighness:", self.brightness, "\n")

    def __init__(self, token):
        self.lights = []
        self.lightsDict = {}
        self.token = token
        self.headers = {
            "Authorization": "Bearer %s" % token,
        }

        jsonObject = json.loads(requests.get('https://api.lifx.com/v1/lights/all', headers=self.headers).text)
        for i in range(0, len(jsonObject)):
            self.lights.append(easyLIFX.Light(jsonObject[i]["id"], jsonObject[i]["label"], jsonObject[i]["power"], jsonObject[i]["brightness"]))
            self.lightsDict[jsonObject[i]["label"].lower()] = jsonObject[i]["id"]

    # Prints known info about lights from Light class
    def listLightsInfo(self):
        print("Lights Connected:", len(self.lights), "\n")
        for light in self.lights:
            light.printInfo()

    # Power switch, lights keep their set values
    def togglePower(self, lights="all"):
        lightsID = self.parseLightLabel(lights)

        requests.post('https://api.lifx.com/v1/lights/%s/toggle' % lightsID, headers=self.headers)

    # Set light state, optional values
    def setState(self, state="on", brightness="1.0", duration="1", color="kelvin:4500", lights="all"):
        lightsID = self.parseLightLabel(lights)

        payload = {
            "power": state,
            "color": color,
            "brightness": brightness,
            "duration": duration
        }

        requests.put('https://api.lifx.com/v1/lights/%s/state' % lightsID, data=payload, headers=self.headers)

    # Lookup light ID based on logical label, e.g. "Bed"
    def lookupByLabel(self, name):
        try:
            return self.lightsDict[name.lower().strip()]
        except KeyError:
            return "%s - Not Found" % name

    # Convert comma seperated light names to their repective IDs
    # Preferred format: "Bed,Desk"
    def parseLightLabel(self, lightLabel):
        if lightLabel.lower() == "all":
            return "all"
        else:
            idString = ""
            for name in lightLabel.split(","):
                idString += self.lookupByLabel(name) + ","

            return idString[:-1]
