#include "PulseWidth.h"
#include <stdexcept>

void PulseWidth::define(float min, float max, float steady) 
{ 
    this->min = min; 
    this->max = max;
    this->steady = steady; 
}

bool PulseWidth::isDefined() 
{
    if (this->min == -1 || this->max == -1 || this->steady == -1) return false;
    return true;
}

float PulseWidth::validate(float pulseWidth) 
{
    if (pulseWidth > this->max) return this->max;
    if (pulseWidth < this->min) return this->min;
}