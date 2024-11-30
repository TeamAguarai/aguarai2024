#include "gpio.h"

namespace control {
    void setup() {
        int pwmPin = 12;
        
        gpio::pinMode(pwmPin, gpio::PWM_OUTPUT);
    }

    void setMotorSpeed(double pulseWidthMs) {
        

        gpio::pwmWrite(pwmPin, pulseWidthMs);
    }

    void getSpeed() {

    }

}




#include <wiringPi.h>
#include <stdio.h>
#include <time.h>

#define SENSOR_PIN 4 // Pin GPIO donde está conectado el sensor
#define WHEEL_CIRCUMFERENCE 0.0545 * 2 * 3.1416 // Circunferencia de la rueda en metros

// Variables globales
volatile double timeInterval = 0.0;
volatile double speed = 0.0;
struct timespec startTime, endTime;

// Calcula la velocidad en m/s
double calculateSpeed(double timeIntervalSeconds) {
    if (timeIntervalSeconds > 0) {
        return WHEEL_CIRCUMFERENCE / timeIntervalSeconds;
    }
    return 0.0; // Evita divisiones por cero
}

// Interrupción: Calcula la velocidad
void pulseHandler() {
    clock_gettime(CLOCK_MONOTONIC, &endTime);
    timeInterval = (endTime.tv_sec - startTime.tv_sec) +
                   (endTime.tv_nsec - startTime.tv_nsec) / 1e9;

    speed = WHEEL_CIRCUMFERENCE / timeIntervalSeconds;

    // Imprime la velocidad (usa con cuidado en interrupciones)
    printf("Velocidad: %.3f m/s\n", speed);

    // Actualiza el tiempo del último pulso
    clock_gettime(CLOCK_MONOTONIC, &startTime);
}

int main() {
    // Inicializa WiringPi
    if (wiringPiSetupGpio() == -1) {
        printf("Error al inicializar WiringPi\n");
        return 1;
    }

    // Configura el pin del sensor como entrada y asigna interrupción
    pinMode(SENSOR_PIN, INPUT);
    wiringPiISR(SENSOR_PIN, INT_EDGE_RISING, &pulseHandler);

    // Inicializa el tiempo
    clock_gettime(CLOCK_MONOTONIC, &startTime);

    printf("Iniciando...\n");

    // Bucle principal
    while (1) {
        delay(100); // Pausa para evitar sobrecargar el procesador
    }

    return 0;
}
