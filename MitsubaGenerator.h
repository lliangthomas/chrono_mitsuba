#pragma once

#if ((defined _WIN32) || (defined(__MINGW32__) || defined(__CYGWIN__))) 
#define APIEXPORT __declspec(dllexport)
#else
#define APIEXPORT
#endif

#include <libxml/encoding.h>
#include <libxml/xmlwriter.h>

using namespace std;

struct xml {
    xml(string type_, string parameter_, string value_) : type(type_), parameter(parameter_), value(value_) {}
    string type;
    string parameter;
    string value;
}