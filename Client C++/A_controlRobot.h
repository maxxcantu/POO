
/* 
 * File:   A_controlRobot.h
 * Author: maxx
 *
 * Created on 16 de marzo de 2022, 21:04
 */

#ifndef A_CONTROLROBOT_H
#define A_CONTROLROBOT_H


#include "A_librerias.h"


class ControlRobot {
private:
    string url;
    XmlRpcClient* cliente;
    XmlRpcValue resultado;
    XmlRpcValue noArgs;
    XmlRpcValue act;
    XmlRpcValue des;
    XmlRpcValue m_vinc;
    XmlRpcValue m_ef;
    XmlRpcValue m_a;
 
    string serverUrl = "0";
    bool flag_conexion = false;
    bool flag_ma = false; //Para la lectura de archivo
    string comandos;
    string mensaje;


public:
    ControlRobot(XmlRpcClient*& cliente);
    ~ControlRobot();

    void conexion();
    void desconexion();
    void listado();
    void ayuda();
    void activacion();
    void desactivacion();
    void modo_vinculo(double q1, double q2, double q3, double qv1, double qv2, double qv3);
    void modo_efector(double x, double y, double a, double t);
    void modo_homing();
    void modo_automatico(int f);


};

#endif /* A_CONTROLROBOT_H */

