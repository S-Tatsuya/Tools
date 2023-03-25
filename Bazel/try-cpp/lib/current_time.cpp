#include "current_time.h"
#include <iostream>
#include <sstream>

std::string getDatetimeStr()
{
    time_t t = time(nullptr);
    const tm* localTime = localtime(&t);
    std::stringstream s;
    s << localTime->tm_year + 1900;
    // setw(),setfill()で0詰め
    s << localTime->tm_mon + 1;
    s << localTime->tm_mday;
    s << localTime->tm_hour;
    s << localTime->tm_min;
    s << localTime->tm_sec;
    // std::stringにして値を返す
    return s.str();
}
