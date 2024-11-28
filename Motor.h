#include "PulseWidth.h"

class Motor
{
private:
    
public:
    PulseWidth pulseWidth;
    int pin;
    Motor(int);
    void setSpeed(float pulseWidth);
    ~Motor();
};