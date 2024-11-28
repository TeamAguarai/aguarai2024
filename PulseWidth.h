class PulseWidth
{
public:
    float min = -1; // -1 como valor indefinido
    float max = -1;
    float steady = -1;
    void define(float, float, float);
    bool isDefined();
    float validate(float);
};
