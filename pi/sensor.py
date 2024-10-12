import smbus
from arduino_interface import get_signals
from constants import BUS_NUMBER

class Sensor:
    def __init__(self, arduino_port, i2c_address=0x04) -> None:
        self.bus = smbus.SMBus(BUS_NUMBER)
        self.arduino_port = arduino_port
        self.i2c_address = i2c_address

    def get_signal(self) -> int:
        return get_signals()[]