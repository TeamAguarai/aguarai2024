import RPi.GPIO as GPIO
import time, math

# Configuración de la numeración de pines
GPIO.setmode(GPIO.BOARD)  # Usa la numeración BCM (números GPIO)

# Define el pin de entrada
HALL_SENSOR_PIN = 5  # Usa el pin GPIO 17, puedes cambiarlo según tu conexión

# Configura el pin como entrada
GPIO.setup(HALL_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
vueltas = 0
distancia_total = 0
ultima_lectura = time.time()
circunferencia_rueda = math.pi * 0.047

def contar_vuelta(channel):
    global vueltas, ultima_lectura, distancia_total
    vueltas += 1
    distancia_total += circunferencia_rueda
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - ultima_lectura
    ultima_lectura = tiempo_actual
    
    # Cálculo de la velocidad (m/s)
    if tiempo_transcurrido > 0:
        velocidad = circunferencia_rueda / tiempo_transcurrido
    else:
        velocidad = 0
    
    # Imprimir resultados
    print(f"Vueltas: {vueltas}")
    print(f"Distancia recorrida: {distancia_total:.2f} metros")
    print(f"Velocidad: {velocidad:.2f} m/s\n")



if __name__ == "__main__":
    try:
        GPIO.add_event_detect(HALL_SENSOR_PIN, GPIO.FALLING, callback=contar_vuelta)

        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Programa interrumpido")

    finally:
        # Limpia los pines GPIO al salir
        GPIO.cleanup()
