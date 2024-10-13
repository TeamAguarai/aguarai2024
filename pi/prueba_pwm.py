import pigpio
import time
from tests2 import Reader
import sys
# Configurar el pin GPIO para PWM
PWM_PIN = 18  # Pin GPIO que utilizará PWM (recomendado GPIO 18)
pi = pigpio.pi()

if not pi.connected:
    exit()

try:
    while True:
        # Pedir al usuario que ingrese el ciclo de trabajo en microsegundos
        duty_cycle = int(input("Ingrese el ciclo de trabajo (1000 a 2000 microsegundos): "))

        # Verificar si el valor está dentro del rango adecuado
        if 1000 <= duty_cycle <= 2000:
            # Establecer el ciclo de trabajo directamente en microsegundos
            pi.set_servo_pulsewidth(PWM_PIN, duty_cycle)
            print(f"PWM ajustado a {duty_cycle} microsegundos.")
        else:
            print("Por favor, ingrese un valor entre 1000 y 2000 microsegundos.")

except KeyboardInterrupt:
    # Detener la señal PWM y limpiar
    pi.stop()  # Detener pigpio
    print("\nSeñal PWM detenida.")


# if __name__ == "__main__":
#     RPM_GPIO = 17  # Cambia este valor al pin adecuado de tu sensor de efecto Hall
#     PULSES_PER_REVOLUTION = 2  # Cambia este valor según tu sensor
#     WHEEL_PERIMETER = 0.105  # Perímetro de la rueda en metros
#     SAMPLE_TIME = 0.1  # Tiempo de muestreo

#     reader = Reader(RPM_GPIO, PULSES_PER_REVOLUTION, WHEEL_PERIMETER, SAMPLE_TIME)

#     try:
#         while True:
#             rpm_value = reader.rpm()

#             if rpm_value is not None:
#                 distance = reader.get_distance()
#                 total_pulse_count = reader.get_total_pulse_count()

#                 duty_cycle = int(input("\n\nIngrese el ciclo de trabajo (1000 a 2000 microsegundos): "))

#                 # Verificar si el valor está dentro del rango adecuado
#                 if 1000 <= duty_cycle <= 2000:
#                     # Establecer el ciclo de trabajo directamente en microsegundos
#                     pi.set_servo_pulsewidth(PWM_PIN, duty_cycle)
#                 else:
#                     print("Por favor, ingrese un valor entre 1000 y 2000 microsegundos.")

#                 # Imprimir en una sola línea con actualización en tiempo real
#                 sys.stdout.write(f"\rRPM: {rpm_value:.2f} | Distancia: {distance:.2f} m | Pulsos totales: {total_pulse_count}")
#                 sys.stdout.flush()

#     except KeyboardInterrupt:
#         print("\nPrograma terminado.")
#         reader.cleanup()
