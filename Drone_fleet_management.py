class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def display_info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Drone is flying...")

class Drone(Device, Flyer):
    def __init__(self, device_id, model):
        super().__init__(device_id)
        self.model = model

    def capture_image(self):
        print("Image captured by the drone.")

    def display_info(self):
        super().display_info()
        print(f"Drone Model: {self.model}")

if __name__ == "__main__":
    d1 = Drone("DR123", "XPro-9")
    d1.display_info()
    d1.fly()
    d1.capture_image()
