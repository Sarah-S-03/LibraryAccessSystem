class Appliance:
    def status(self):
        print("Generic appliance status")

class Fan(Appliance):
    def status(self):
        print("Fan is spinning")

class Light(Appliance):
    def status(self):
        print("Light is on")

class AC(Appliance):
    def status(self):
        print("AC is cooling")

devices = [Fan(), Light(), AC()]
for device in devices:
    device.status()
