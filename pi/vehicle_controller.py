from sensor import Sensor

class VehicleController:
    def __init__(self, enconder: Sensor):
        self.encoder = enconder

    def initialize_system(self):
        pass

    def test(self):
        print(self.encoder.get_signal())