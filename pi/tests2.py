import pigpio
import time
import sys

class Reader:
    def __init__(self, gpio_pin, pulses_per_revolution=2, wheel_perimeter=0.2, sample_time=0.5):
        self.gpio_pin = gpio_pin
        self.sample_time = sample_time
        self.pulse_count = 0
        self.total_pulse_count = 0  # Conteo total de pulsos
        self.start_time = time.time()
        self.total_revolutions = 0
        self.pulses_per_revolution = pulses_per_revolution  # Número de pulsos por revolución
        self.wheel_perimeter = wheel_perimeter  # Perímetro de la rueda (en metros)
        self.distance = 0  # Distancia total recorrida

        # Iniciar pigpio
        self.pi = pigpio.pi()

        # Configuración del pin como entrada y con pull-up
        self.pi.set_mode(self.gpio_pin, pigpio.INPUT)
        self.pi.set_pull_up_down(self.gpio_pin, pigpio.PUD_UP)

        # Detectar el flanco descendente (de 1 a 0) cuando el imán pasa por el sensor
        self.pi.callback(self.gpio_pin, pigpio.FALLING_EDGE, self._pulse_detected)

    def _pulse_detected(self, gpio, level, tick):
        """Función llamada en cada flanco de bajada (FALLING_EDGE) detectado."""
        self.pulse_count += 1
        self.total_pulse_count += 1  # Incrementar el conteo total de pulsos

    def rpm(self):
        """Calcula las RPM (revoluciones por minuto) en función del número de pulsos detectados."""
        elapsed_time = time.time() - self.start_time

        if elapsed_time >= self.sample_time:
            # Calcular las RPM
            rpm_value = (self.pulse_count / self.pulses_per_revolution) / elapsed_time * 60
            # Calcular las revoluciones totales
            revolutions = self.pulse_count / self.pulses_per_revolution
            self.total_revolutions += revolutions
            # Calcular la distancia recorrida
            self.distance += revolutions * self.wheel_perimeter

            # Reiniciar el contador de pulsos y el tiempo
            self.pulse_count = 0
            self.start_time = time.time()

            return rpm_value
        else:
            return None

    def get_distance(self):
        """Retorna la distancia total recorrida en metros."""
        return self.distance

    def get_total_pulse_count(self):
        """Retorna el número total de pulsos detectados."""
        return self.total_pulse_count

    def cleanup(self):
        """Limpia el sistema pigpio y detiene el demonio."""
        self.pi.stop()

# Ejemplo de uso:
if __name__ == "__main__":
    RPM_GPIO = 17  # Cambia este valor al pin adecuado de tu sensor de efecto Hall
    PULSES_PER_REVOLUTION = 2  # Cambia este valor según tu sensor
    WHEEL_PERIMETER = 0.105  # Perímetro de la rueda en metros
    SAMPLE_TIME = 0.1  # Tiempo de muestreo

    reader = Reader(RPM_GPIO, PULSES_PER_REVOLUTION, WHEEL_PERIMETER, SAMPLE_TIME)

    try:
        while True:
            rpm_value = reader.rpm()

            if rpm_value is not None:
                distance = reader.get_distance()
                total_pulse_count = reader.get_total_pulse_count()

                # Imprimir en una sola línea con actualización en tiempo real
                sys.stdout.write(f"\rRPM: {rpm_value:.2f} | Distancia: {distance:.2f} m | Pulsos totales: {total_pulse_count}")
                sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nPrograma terminado.")
        reader.cleanup()
