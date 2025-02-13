
#include "FmtMaster.h"

#include <fmt/core.h>

void FmtMaster::Print(std::string&& msg)
{
    fmt::print("{}\n", msg);
}
