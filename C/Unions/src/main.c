#include <stdio.h>

// An example of using a union to represent an 8-bit register
union Register 
{
    struct 
    {
        unsigned char b0: 1;
        unsigned char b1: 1;
        unsigned char b2: 1;
        unsigned char b3: 1;
        unsigned char b4: 1;
        unsigned char b5: 1;
        unsigned char b6: 1;
        unsigned char b7: 1;
    } bits;
    unsigned char value;
} reg;

int main()
{
    reg.value = 24;

    printf("value:  %d, size of reg.bits in bytes:  %d\n", 
    reg.value, 
    sizeof(reg.bits));

    // manipulate individual bits (little endian)
    reg.bits.b0 = 1;
    reg.bits.b1 = 0;
    reg.bits.b2 = 1;
    reg.bits.b3 = 1;
    reg.bits.b4 = 1;
    reg.bits.b5 = 0;
    reg.bits.b6 = 0;
    reg.bits.b7 = 1;

    printf("value: %d, size of reg.value in bytes: %d\n", 
    reg.value, 
    sizeof(reg.value));
        
    return 0;
}