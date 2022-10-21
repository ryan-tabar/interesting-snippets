#include <stdio.h>

union Register {
    struct {
        unsigned char b0: 1;
        unsigned char b1: 1;
        unsigned char b2: 1;
        unsigned char b3: 1;
        unsigned char b4: 1;
        unsigned char b5: 1;
        unsigned char b6: 1;
        unsigned char b7: 1;
    } bits;
    unsigned char buffer;
} reg;

int main()
{
    reg.buffer = 24;

    printf("value of reg: %d, size of reg.bits in bytes: %d\n", reg.buffer, sizeof(reg.bits));

    // manipulate individual bits
    reg.bits.b0 = 1;
    reg.bits.b1 = 0;
    reg.bits.b2 = 1;
    reg.bits.b3 = 1;
    reg.bits.b5 = 1;
    reg.bits.b6 = 1;
    reg.bits.b7 = 0;

    printf("value of buffer: %d size of reg.buffer in bytes: %d\n", reg.buffer, sizeof(reg.buffer));
        
    return 0;
}