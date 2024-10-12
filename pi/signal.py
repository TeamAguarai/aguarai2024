import smbus
import time

# Dirección del esclavo Arduino (en este caso, es 8)
I2C_ADDRESS = 0x08
# Crear objeto de bus I2C
bus = smbus.SMBus(1)  # Usar bus 1 para Raspberry Pi

def get_signal():
    try:
        # Lee 2 bytes del Arduino
        data = bus.read_i2c_block_data(I2C_ADDRESS, 0, 2)
        
        # Combina los dos bytes para formar el valor entero
        valor_entero = (data[0] << 8) | data[1]
        return valor_entero
    except Exception as e:
        print(f"Error al leer datos del Arduino: {e}")
        return None

# Ejemplo de uso de la función
while True:
    valor = leer_senal_arduino()
    if valor is not None:
        print(valor)
    time.sleep(0.001)  # Espera de 1 segundo antes de la siguiente lectura
