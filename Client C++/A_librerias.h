/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/cppFiles/file.h to edit this template
 */

/* 
 * File:   A_librerias.h
 * Author: maxx
 *
 * Created on 16 de marzo de 2022, 21:00
 */

#ifndef A_LIBRERIAS_H
#define A_LIBRERIAS_H

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <iterator>
#include <ctime>
#include <stdlib.h> 


#include "XmlRpc.h"
using namespace XmlRpc;


using namespace std;

enum Comandos {
    CONEXION, DESCONEXION, LISTADO, AYUDA, ACTIVACION, DESACTIVACION,
    MODO_VINCULOS, MODO_EFECTOR, MODO_HOMING, MODO_AUTOMATICO
};


#endif /* A_LIBRERIAS_H */

