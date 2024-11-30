#ifndef VELOCIMETER_H
#define VELOCIMETER_H

#include <time.h>

class Velocimeter
{
private:
    double wheelCircumference;
    double timeInterval;
    struct timespec startTime, endTime;
    static void pulseHandlerWrapper();
public:
    int pin;
    double speed;
    double wheelDiameter;
    Velocimeter(int, double);
    void pulseHandler();
    void start();
};

#endif