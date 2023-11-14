
#include "C_interfaz.h"

Interfaz::Interfaz() {
}

string Interfaz::menu(ControlRobot*& controlador) {
    string comandos;
    Identificador* id_ord = new Identificador();

    cout << "\n\n-----------------------------------------------------------------------------"
            "\n----                        CONTROL REMOTO DE ROBOT                       ---"
            "\n-----------------------------------------------------------------------------"
            "\nIntroducir los comandos para cada instrucción:"
            "\nConexión al servidor: C"
            "\nMenu de ayuda: A"
            "\nCerrar el programa: exit"
            "\n >>> ";
    cin >> comandos;
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";

    if (comandos[0] == 'e' && comandos[1] == 'x' && comandos[2] == 'i' && comandos[3] == 't') {
        return comandos;
    }
    else {
        id_ord->id(comandos, vec);
        this->realizar(controlador);
        return comandos;
    }
    delete id_ord;
}

void Interfaz::realizar(ControlRobot*& controlador) {
    for (int i = 0; i < vec.size(); i++) {
        int valor = (int)vec[i];
        switch (valor) {
        case CONEXION:
            controlador->conexion();
            continue;

        case DESCONEXION:
            controlador->desconexion();
            break;

        case LISTADO:
            controlador->listado();
            break;

        case AYUDA:
            controlador->ayuda();
            break;

        case ACTIVACION:
            controlador->activacion();
            break;

        case DESACTIVACION:
            controlador->desactivacion();
            break;

        case MODO_VINCULOS:
            controlador->modo_vinculo(vec[i + 1], vec[i + 2]
                , vec[i + 3], vec[i + 4], vec[i + 5], vec[i + 6]);
            i += 6;
            break;

        case MODO_EFECTOR:
            controlador->modo_efector(vec[i + 1], vec[i + 2]
                , vec[i + 3], vec[i + 4]);
            i += 4;
            break;

        case MODO_HOMING:
            controlador->modo_homing();
            break;

        case MODO_AUTOMATICO:
            controlador->modo_automatico(vec[i + 1]);
            i += 1;
            break;

        default:
            break;
        }
    }


}

Interfaz::~Interfaz() {
}

