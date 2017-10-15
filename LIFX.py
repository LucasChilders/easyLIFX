import requests
import json
import os

class LIFX:
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
            self.lights.append(LIFX.Light(jsonObject[i]["id"], jsonObject[i]["label"], jsonObject[i]["power"], jsonObject[i]["brightness"]))
            self.lightsDict[jsonObject[i]["label"].lower()] = jsonObject[i]["id"]

    def lightLightsInfo(self):
        print("Lights Connected:", len(self.lights), "\n")
        for light in self.lights:
            light.printInfo()

    # Power switch
    def togglePower(self, lightLabel="all"):
        requests.post('https://api.lifx.com/v1/lights/%s/toggle' % lightLabel, headers=self.headers)

    # Set light state, optional values.
    def setState(self, state="on", brightness="1.0", duration="1", color="kelvin:4500", lightLabel="all"):
        payload = {
            "power": state,
            "color": color,
            "brightness": brightness,
            "duration": duration
        }

        requests.put('https://api.lifx.com/v1/lights/%s/state' % lightLabel, data=payload, headers=self.headers)

    # Lookup light ID based on logical label, e.g. "Bed"
    def lookupByLabel(self, name):
        for light in self.lights:
            if light.label.lower() == name.lower():
                return light.id

        return None

    def parseLightLabel(self, lightLabel):
        if lightLabel.lower() == "all":
            return "all"
        else:
            return None

#
lifx = LIFX(os.environ["LIFX_KEY"])

# lifx.setState()
lifx.togglePower()
lifx.lightLightsInfo()
print(lifx.lookupByLabel("Bed"))
