#include <Wire.h>
#include <Arduino.h>

// Dirección I2C del Arduino
const int SLAVE_ADDRESS = 0x04;

// Definir los pines analógicos y digitales
const int analogPins[] = {A0, A1, A2, A3, A4, A5}; // Pines analógicos
const int digitalPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}; // Pines digitales
const int totalPins = sizeof(analogPins) / sizeof(analogPins[0]) + sizeof(digitalPins) / sizeof(digitalPins[0]); // Total de pines

// Esta función se llama cuando el maestro solicita datos
void requestEvent() {
  // Envía los valores de todos los pines
  for (int i = 0; i < sizeof(analogPins) / sizeof(analogPins[0]); i++) {
    Wire.write(analogRead(analogPins[i]) >> 2); // Envía el valor ajustado (0-255)
  }

  for (int i = 0; i < sizeof(digitalPins) / sizeof(digitalPins[0]); i++) {
    Wire.write(digitalRead(digitalPins[i])); // Envía el valor (0 o 1)
  }

  // Envía un byte de fin de transmisión
  Wire.write(0xFF); // Byte de fin de transmisión
}

void setup() {
  Wire.begin(SLAVE_ADDRESS); // Inicia el bus I2C como esclavo
  Wire.onRequest(requestEvent); // Registra la función que se llama cuando el maestro solicita datos

  // Configura los pines digitales como entrada
  for (int i = 0; i < sizeof(digitalPins) / sizeof(digitalPins[0]); i++) {
    pinMode(digitalPins[i], INPUT);
  }
}

void loop() {
  // No se necesita hacer nada en el bucle principal
}