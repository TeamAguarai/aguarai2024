#include "gpio.h"
#include "Velocimeter.h"
#include <iostream>
#include <unordered_map>

int main() {

    gpio::setupGpioPinout();

    Velocimeter velocimeter(2,3.4);
    velocimeter.start();

    while (true)
    {
        /* code */
    }
    

    return 0;
}
