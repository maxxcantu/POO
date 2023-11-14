
/* 
 * File:   B_identificador.h
 * Author: maxx
 *
 * Created on 16 de marzo de 2022, 21:08
 */

#ifndef B_IDENTIFICADOR_H
#define B_IDENTIFICADOR_H

#include "A_controlRobot.h"

class Identificador {
    
public:
    Identificador();
    ~Identificador();
    void id(string ordenes, vector<double>& vec);
};


#endif /* B_IDENTIFICADOR_H */

