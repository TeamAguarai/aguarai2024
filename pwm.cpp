#include <wiringPi.h>
#include <iostream>

// Definir el pin PWM (puedes cambiar este valor según tu configuración)
#define PWM_PIN 12 // GPIO 18 en la Raspberry Pi (canal PWM hardware)

void configurarPWM(double frecuencia, double anchoPulsoMs) {
    // Calcular el rango (resolución) y el divisor para ajustar la frecuencia
    double periodoMs = 1000.0 / frecuencia; // Periodo en milisegundos
    int rango = 1024; // Resolución del PWM (por defecto en wiringPi)
    int divisor = static_cast<int>(19200000.0 / (frecuencia * rango)); // PWM clock a 19.2 MHz

    // Inicializar wiringPi
    if (wiringPiSetupGpio() == -1) {
        std::cerr << "Error al inicializar wiringPi." << std::endl;
        return;
    }

    // Configurar el pin PWM
    pinMode(PWM_PIN, PWM_OUTPUT);

    // Ajustar el divisor y rango
    pwmSetMode(PWM_MODE_MS);      // Modo "Mark-Space" para precisión
    pwmSetRange(rango);           // Rango para el ciclo de trabajo
    pwmSetClock(divisor);         // Divisor para ajustar la frecuencia

    // Calcular el ciclo de trabajo correspondiente al ancho de pulso deseado
    int cicloTrabajo = static_cast<int>((anchoPulsoMs / periodoMs) * rango);

    // Establecer el ciclo de trabajo
    pwmWrite(PWM_PIN, cicloTrabajo);

    // Mensaje informativo
    std::cout << "PWM configurado:" << std::endl;
    std::cout << "Frecuencia: " << frecuencia << " Hz" << std::endl;
    std::cout << "Ancho de Pulso: " << anchoPulsoMs << " ms" << std::endl;
    std::cout << "Periodo: " << periodoMs << " ms" << std::endl;
    std::cout << "Ciclo de Trabajo: " << cicloTrabajo << "/" << rango << std::endl;
}

int main() {
    // Configurar PWM con los datos del osciloscopio
    double frecuencia = 76.92;    // Frecuencia en Hz
    double anchoPulsoMs = 1.52;   // Ancho de pulso en milisegundos

    configurarPWM(frecuencia, anchoPulsoMs);

    // Mantener el programa activo para que el PWM continúe
    while (true) {
        printf("Ingrese el nuevo ancho de pulso (ms): ");
        if (scanf("%lf", &anchoPulsoMs) != 1 || anchoPulsoMs <= 0) {
            fprintf(stderr, "Error: Debe ingresar un valor válido mayor que 0.\n");
            while (getchar() != '\n'); // Limpiar el buffer de entrada
            continue;
        }
        
        configurarPWM(frecuencia, anchoPulsoMs);
    }

    return 0;
}
