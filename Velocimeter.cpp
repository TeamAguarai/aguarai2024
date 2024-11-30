#include "Velocimeter.h"
#include "gpio.h"
#include <iostream>
#include <chrono>

Velocimeter* velocimeterInstance = nullptr;

Velocimeter::Velocimeter(int pin, double wheelDiameter) : pin(pin), wheelDiameter(wheelDiameter)
{
    this->wheelCircumference = 2 * (wheelDiameter/2) * 3.1416;
    velocimeterInstance = this;
}

void Velocimeter::pulseHandlerWrapper() {
    velocimeterInstance->pulseHandler();
}

void Velocimeter::pulseHandler() {
    std::cout << "PULSE HANDLER" << std::endl;
    // clock_gettime(CLOCK_MONOTONIC, &this->endTime);
    // this->timeInterval = (endTime.tv_sec - startTime.tv_sec) +
    //                (endTime.tv_nsec - startTime.tv_nsec) / 1e9;

    // this->speed = (timeInterval > 0) ? (this->wheelCircumference / this->timeInterval) : 0.0;

    // // Actualiza el tiempo del último pulso
    // clock_gettime(CLOCK_MONOTONIC, &startTime);
}
 
void Velocimeter::start() {
    gpio::pinMode(this->pin, gpio::INPUT);

    gpio::onInterrupt(this->pin, gpio::INT_EDGE_RISING, &pulseHandlerWrapper );
    // if (wiringPiISR(pin, INT_EDGE_RISING, static_cast<void (*)(void)>([=]() { staticPulseHandler(pin); })) < 0) {
    //     std::cerr << "Error configuring ISR for pin " << pin << std::endl;
    // }
    // Inicializa el tiempo
    clock_gettime(CLOCK_MONOTONIC, &this->startTime);
}
