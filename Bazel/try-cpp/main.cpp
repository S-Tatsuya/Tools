#include <iostream>
#include "output.h"
#include "current_time/current_time.h"

int main(void)
{
    output(getDatetimeStr());
    output("Hello world.");
    return 0;
}
