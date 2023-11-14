

#include "A_librerias.h"
#include "A_controlRobot.h"
#include "C_interfaz.h"

int main(int argc, char** argv) {
    if (argc != 3) {
    	cerr << "Uso: hola_Client IP_HOST N_PORT\n";
    return -1;
    }
    int port = atoi(argv[2]);
    
    XmlRpcClient* cliente = new XmlRpcClient(argv[1], port);

    string comandos;

    ControlRobot* controlador = new ControlRobot(cliente);

    Interfaz* interfaz = new Interfaz();

    while (true) {
        comandos = interfaz->menu(controlador);

        if (comandos[0] == 'e' && comandos[1] == 'x' && comandos[2] == 'i' && comandos[3] == 't') {
            cout << endl << "El programa se cerrará..." << endl;
            delete interfaz;
            delete controlador;
            break;
        }
    }
    return 0;
}
