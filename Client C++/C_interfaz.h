
/* 
 * File:   C_interfaz.h
 * Author: maxx
 *
 * Created on 16 de marzo de 2022, 21:10
 */

#ifndef C_INTERFAZ_H
#define C_INTERFAZ_H

#include "A_controlRobot.h"
#include "B_identificador.h"
using namespace std;

class Interfaz {
public:
    Interfaz();
    ~Interfaz();
    string menu(ControlRobot*&);
    void realizar(ControlRobot*&);
    
    vector<double> vec;
};


#endif /* C_INTERFAZ_H */

