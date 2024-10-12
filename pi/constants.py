import json

# Open and read the JSON file
with open('../shared/config.json', 'r') as file:
    CONFIG = json.load(file)

I2CBUS_NUMBER = CONFIG.i2cBusNumber
ENCODER_ADDR = CONFIG.addresses.encoder