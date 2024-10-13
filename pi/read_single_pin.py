import RPi.GPIO as GPIO
import time

# Configurar el pin GPIO
PIN = 17  # Número del pin GPIO que deseas leer (usar numeración BCM)

GPIO.setmode(GPIO.BCM)  # Usar numeración BCM
GPIO.setup(PIN, GPIO.IN)  # Configurar el pin como entrada

try:
    while True:
        # Leer el estado del pin (0 o 1)
        pin_value = GPIO.input(PIN)

        # Imprimir el valor leído
        print(f"Valor del pin GPIO {PIN}: {pin_value}")

        time.sleep(0.3)  # Esperar 1 segundo antes de la siguiente lectura

except KeyboardInterrupt:
    # Limpiar la configuración GPIO al terminar
    GPIO.cleanup()
    print("Lectura detenida y GPIO limpiado.")
