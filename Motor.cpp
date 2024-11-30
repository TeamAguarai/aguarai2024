#include <stdexcept>
#include "PulseWidth.h"
#include "Motor.h"
#include "gpio.h"

Motor::Motor(int pin) : pin(pin) 
{
    gpio::pinMode(this->pin, gpio::PWM_OUTPUT);
}

void Motor::setSpeed(float pulseWidth) 
{
    if (this->pulseWidth.isDefined() == false) throw std::invalid_argument( "You must fully define motor pulse-width values." );
    
    float _pulseWidth = this->pulseWidth.validate(pulseWidth);
    
    gpio::pwmWrite(this->pin, _pulseWidth);
}

Motor::~Motor()
{
}