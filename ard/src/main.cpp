#include <Arduino.h>
#include <Wire.h>


void loop() {
  // No necesitamos hacer nada en loop porque la función mandarSeñal
  // será llamada automáticamente cuando se solicite desde el maestro.
  delay(1); // Solo para hacer más lento el ciclo
}

// Función que se ejecuta cuando la Raspberry Pi solicita datos
void mandarSenhal() {
  int valorAnalogo = analogRead(A0); // Leer el valor del sensor en el pin A0

  // Enviar el valor como dos bytes (dividir el valor en parte alta y baja)
  Wire.write(valorAnalogo >> 8);    // Enviar el byte alto (bits 9-16)
  Wire.write(valorAnalogo & 0xFF);  // Enviar el byte bajo (bits 1-8)
}

void setup() {
  Wire.begin(8); // Iniciar el Arduino como esclavo con la dirección 8
  Wire.onRequest(mandarSenhal); // Llama a mandarSeñal cuando el maestro (Raspberry Pi) solicita datos
  Serial.begin(9600); // Inicializar comunicación serial para depuración
}
