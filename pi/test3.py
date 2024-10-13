import pigpio
import time

class MotorController:
    def __init__(self, esc_gpio, pi):
        """Inicializa el controlador del motor con el pin ESC y la instancia de pigpio."""
        self.esc_gpio = esc_gpio
        self.pi = pi
        self.calibrate_esc()

    def calibrate_esc(self):
        """Calibra el ESC con los valores mínimos y máximos."""
        print("Calibrando ESC...")
        self.pi.set_servo_pulsewidth(self.esc_gpio, 2000)  # Máxima aceleración.
        time.sleep(2)
        self.pi.set_servo_pulsewidth(self.esc_gpio, 1000)  # Mínima aceleración.
        time.sleep(2)
        print("Calibración completada.")

    def set_speed(self, speed_percentage):
        """Establece la velocidad del motor en función del porcentaje ingresado."""
        # Asegurarse de que el porcentaje esté entre 0 y 100
        if 0 <= speed_percentage <= 100:
            # Convertir porcentaje a ancho de pulso PWM (1000 a 2000 microsegundos)
            pulse_width = speed_percentage * 1000 / 100 + 1000
            self.pi.set_servo_pulsewidth(self.esc_gpio, pulse_width)
            print(f"Velocidad ajustada al {speed_percentage}% ({pulse_width} microsegundos)")
        else:
            print("Por favor, ingrese un valor entre 0 y 100.")

    def stop_motor(self):
        """Detiene el motor configurando el ancho de pulso en 0."""
        self.pi.set_servo_pulsewidth(self.esc_gpio, 0)
        print("Motor detenido.")

# Ejemplo de uso:
if __name__ == "__main__":
    ESC_GPIO = 18  # Cambia este valor según tu pin ESC
    pi = pigpio.pi()

    motor_controller = MotorController(ESC_GPIO, pi)

    try:
        while True:
            # Pedir al usuario la velocidad en porcentaje
            speed_percentage = float(input("Ingrese la velocidad en porcentaje (0 a 100): "))
            motor_controller.set_speed(speed_percentage)

    except KeyboardInterrupt:
        print("\nFinalizando...")
        motor_controller.stop_motor()
        pi.stop()
