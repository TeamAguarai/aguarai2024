#ifndef PULSEWIDTH_H
#define PULSEWIDTH_H

class PulseWidth
{
public:
    double min = -1; // -1 como valor indefinido
    double max = -1;
    double steady = -1;
    void define(double, double, double);
    bool isDefined();
    double validate(double);
};
#endif