import smbus

def get_signals(address) -> dict:
    bus = smbus.SMBus(1)  # Inicializa el bus I2C
    data_dict = {}  # Diccionario para almacenar los valores

    bus.write_byte(address, address)  # Envía la dirección del Arduino

    # Lee todos los datos enviados por el Arduino
    index = 0
    while True:
        try:
            value = bus.read_byte(address)  # Lee un byte del Arduino
            if value == 0xFF:  # Verifica el byte de fin de transmisión
                break  # Sale del bucle si se recibe el byte de fin
            data_dict[f'pin_{index}'] = value  # Almacena el valor en el diccionario
            index += 1
        except OSError:
            break  # Rompe el bucle si hay un error en la lectura

    return data_dict

while True:
    print(get_signals())