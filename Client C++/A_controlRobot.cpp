
#include "A_controlRobot.h"


ControlRobot::ControlRobot(XmlRpcClient*& cliente) {
    this->cliente = cliente;
}

void ControlRobot::conexion() {
    if (!flag_conexion) {
        serverUrl = "http://";
        cout << endl << "Introducir IP nuevamente:\n" <<  endl;
        cin >> url;
        serverUrl += url;
        serverUrl += ":8890/RPC2";
        flag_conexion = true;
        cout << "\nConectado al servidor satisfactoriamente!";
    }
    else {
        cout << "\nYa estamos conectados al servidor." << endl << endl;
    }
}

void ControlRobot::desconexion() {
    if (flag_conexion) {
        flag_conexion = false;
        cout << "\nSe ha deconectado del servidor" << endl << endl;
    }
    else {
        cout << "\nYa estamos deconectado del servidor." << endl << endl;
    }
}

void ControlRobot::listado() {
    if (flag_conexion) {
        if (cliente->execute("reporte", noArgs, resultado)) { 
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::ayuda() {
    if (flag_conexion) {
        if (cliente->execute("ayuda", noArgs, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::activacion() {
    if (flag_conexion) {
        act[0] = true;
        if (cliente->execute("activacion_desactivacion", act, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::desactivacion() {
    if (flag_conexion) {
    	des[0] = false;
        if (cliente->execute("activacion_desactivacion", des, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::modo_vinculo(double q1, double  q2, double q3, double v1, double v2, double v3) {
    if (flag_conexion) {
        m_vinc[0] = q1;
        m_vinc[1] = q2;
        m_vinc[2] = q3;
        m_vinc[3] = v1;
        m_vinc[4] = v2;
        m_vinc[5] = v3;
        if (cliente->execute("modo_vinculo", m_vinc, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::modo_efector(double x, double y, double a, double t) {
    if (flag_conexion) {
        m_ef[0] = x;
        m_ef[1] = y;
        m_ef[2] = a;
        m_ef[3] = t;
        if (cliente->execute("modo_efector", m_ef, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::modo_homing() {
    if (flag_conexion) {
        if (cliente->execute("modo_homing", noArgs, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

void ControlRobot::modo_automatico(int f) {
    m_a[0] = f;
    string ma_archivo = "modo_auto_" + to_string(f) + ".txt";
    cout << "\n>>> Se realizarán las instrucciones del archivo: " << ma_archivo; 
    if (flag_conexion) {
        if (cliente->execute("modo_automatico", m_a, resultado)) {
            cout << resultado << endl << endl;
        }
    }
    else {
        cout << "\nNo estamos conectados a ningún servidor." << endl << endl;
    }
}

ControlRobot::~ControlRobot() {
}
