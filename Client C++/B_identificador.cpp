
#include "B_identificador.h"


Identificador::Identificador() {
}

void Identificador::id(string ordenes, vector<double>& vec) {
    //this->vec = vec;
    vec.clear();
    int longitud = ordenes.length();
    vector<double>::iterator it1, it2;
    double numero;
    int cont = 0;
    bool flag1 = false, flag2 = false;
    int i = 0;
    while (!ordenes.empty()) {
        switch (ordenes[0]) {
        case 'c':
        case 'C':
            vec.push_back(CONEXION);
            i++;
            ordenes.erase(0, 1);
            break;
        case 'd':
        case 'D':
            switch (ordenes[1]) {
            case 'e':
            case 'E':
                vec.push_back(DESACTIVACION);
                i++;
                ordenes.erase(0, 2);
                break;
            case '-':
                vec.push_back(DESCONEXION);
                i++;
                ordenes.erase(0, 1);
                break;
            case NULL:
                vec.push_back(DESCONEXION);
                i++;
                ordenes.erase(0, 1);
                break;
            case '\n':
                vec.push_back(DESCONEXION);
                i++;
                ordenes.erase(0, 1);
                break;
            case '\\n':
                vec.push_back(DESCONEXION);
                i++;
                ordenes.erase(0, 1);
                break;
            default:
                ordenes.erase(0, 1);
                break;
            }
            break;
        case 'l':
        case 'L':
            vec.push_back(LISTADO);
            i++;
            ordenes.erase(0, 1);
            break;
        case 'a':
        case 'A':
            switch (ordenes[1]) {
            case 'c':
            case 'C':
                vec.push_back(ACTIVACION);
                i++;
                ordenes.erase(0, 2);
                break;
            case '-':
                vec.push_back(AYUDA);
                i++;
                ordenes.erase(0, 1);
                break;
            case NULL:
                vec.push_back(AYUDA);
                i++;
                ordenes.erase(0, 1);
                break;
            case '\\n':
                vec.push_back(AYUDA);
                i++;
                ordenes.erase(0, 1);
                break;
            default:
                ordenes.erase(0, 1);
                break;
            }
            break;
        case 'm':
        case 'M':
            switch (ordenes[1]) {
            case 'v':
            case 'V':
                vec.push_back(MODO_VINCULOS);
                i++;
                ordenes.erase(0, 2);
                while (ordenes[0] != '-' && !ordenes.empty()) {
                    numero = stod(ordenes);
                    vec.push_back(numero);
                    i++;
                    cont++;
                    while (ordenes[0] != ',' && !ordenes.empty() && ordenes[0] != '-') {
                        ordenes.erase(0, 1);
                    }
                    if (ordenes[0] == ',') {
                        ordenes.erase(0, 1);
                    }
                }
                ordenes.erase(0, 1);
                if (cont != 6) {
                    i = i - (cont + 1);
                    it1 = vec.begin();
                    it1 += i;
                    it2 = it1;
                    it2 += (cont + 1);
                    vec.erase(it1, it2);
                }
                cont = 0;
                break;
            case 'e':
            case 'E':
                vec.push_back(MODO_EFECTOR);
                i++;
                ordenes.erase(0, 2);
                while (ordenes[0] != '-' && !ordenes.empty()) {
                    numero = stod(ordenes);
                    vec.push_back(numero);
                    i++;
                    cont++;
                    while (ordenes[0] != ',' && !ordenes.empty() && ordenes[0] != '-') {
                        ordenes.erase(0, 1);
                    }
                    if (ordenes[0] == ',') {
                        ordenes.erase(0, 1);
                    }
                }
                ordenes.erase(0, 1);
                if (cont != 4) {
                    i = i - (cont + 1);
                    it1 = vec.begin() + i;
                    it2 = it1 + (cont + 1);
                    vec.erase(it1, it2);
                }
                cont = 0;
                break;
            case 'h':
            case 'H':
                vec.push_back(MODO_HOMING);
                i++;
                ordenes.erase(0, 2);
                break;
            case 'a':
            case 'A':
                vec.push_back(MODO_AUTOMATICO);
                i++;
                ordenes.erase(0, 2);
                while (ordenes[0] != '-' && !ordenes.empty()) {
                    numero = stod(ordenes);
                    vec.push_back(numero);
                    i++;
                    cont++;
                    while (ordenes[0] != ',' && !ordenes.empty() && ordenes[0] != '-') {
                        ordenes.erase(0, 1);
                    }
                    if (ordenes[0] == ',') {
                        ordenes.erase(0, 1);
                    }
                }
                ordenes.erase(0, 1);
                if (cont != 1) {
                    i = i - (cont + 1);
                    it1 = vec.begin() + i;
                    it2 = it1 + (cont + 1);
                    vec.erase(it1, it2);
                }
                cont = 0;
                break;
            }
            break;
        default:
            ordenes.erase(0, 1);
            break;
        }
    }
}

Identificador::~Identificador() {
}
