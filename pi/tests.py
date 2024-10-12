from time import sleep
import pigpio

# Set up BCM GPIO numbering
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Connect to pigpio
pi = pigpio.pi()

# Calibrate ESC
# ESC_GPIO = 12
# pi.set_servo_pulsewidth(ESC_GPIO, 2000)  # Maximum throttle.
# sleep(2)
# pi.set_servo_pulsewidth(ESC_GPIO, 1000)  # Minimum throttle.
# sleep(2)

# Set up RPM reader
RPM_GPIO = 11
SAMPLE_TIME = 0.1
from read_rpm import Reader
tach = Reader(pi, RPM_GPIO)

try:
    while True:
        # Pedir al usuario la velocidad en porcentaje
        # speed_percentage = float(input("Ingrese la velocidad en porcentaje (0 a 100): "))

        # # Asegurarse de que el porcentaje esté entre 0 y 100
        # if 0 <= speed_percentage <= 100:
        #     # Convertir porcentaje a ancho de pulso PWM
        #     pulse_width = speed_percentage * 1000 / 100 + 1000  # Mapea de 1000 a 2000 microsegundos
        #     pi.set_servo_pulsewidth(ESC_GPIO, pulse_width)
        # else:
        #     print("Por favor, ingrese un valor entre 0 y 100.")

        # Leer RPM
        rpm = tach.RPM()

        # Mostrar RPM en la terminal
        print(f"RPM: {rpm}")

        sleep(SAMPLE_TIME)

finally:
    pass
    # pi.set_servo_pulsewidth(ESC_GPIO, 0)  # Detener pulsos al ESC.
    # pi.stop()  # Desconectar pigpio.
