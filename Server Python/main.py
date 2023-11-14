from interfaz import InterfazLocal
from controlRobot import controlRobot
from rpc_server import XmlRpcServer

if __name__ == "__main__":
    print("Seleccionar tipo de control: \n" 
        "1. Local \n"
        "2. Remoto ")
    tipo_control = input()

    controlador = controlRobot()

    if (tipo_control == "Local" or tipo_control == "local" or tipo_control == 1):
        print("\nControl Local inicializado")
        control_local = InterfazLocal(controlador)

        while (True):
            comandos = control_local.realizar()
            if (comandos == "exit"):
                print("Gracias por utilizar la conexión local\n")
                break

    elif (tipo_control == "Remoto" or tipo_control == "remoto" or tipo_control == 2):
        print("\nControl Remoto inicializado")
        print("\nIngresar dirección IP:")
        ip = input()
        print("\nIngresar puerto:")
        puerto = input()

        servidor = XmlRpcServer(controlador, ip, puerto)
        # while (True):
        #     server = SimpleXMLRPCServer((str(ip), int(puerto)), requestHandler=Servidor)
        #     server.register_instance(controlRobot())
        #     server.serve_forever()

           
