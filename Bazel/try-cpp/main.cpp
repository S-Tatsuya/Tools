#include <iostream>
#include "output.h"
#include "lib/current_time.h"

int main(void)
{
    output(getDatetimeStr());
    output("Hello world.");
    return 0;
}
