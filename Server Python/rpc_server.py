from xmlrpc.server import SimpleXMLRPCServer
from servidor import Servidor
from threading import Thread
import socket


class XmlRpcServer(object):
    server = None

    def __init__(self, controlador, ip, port):
        self.contorlador = controlador
        self.ip_usada = ip
        self.puerto_usado = int(port)

        while True:
            try:
                #Creacion del servidor indicando el puerto deseado
                self.server = SimpleXMLRPCServer((self.ip_usada, self.puerto_usado), allow_none = True, logRequests = False, requestHandler=Servidor)
                if self.puerto_usado != int(port):
                    print("Servidor RPC ubicado en puerto no estándar [%d]" % self.puerto_usado)
                break
            except socket.error as e:
                if e.errno == 98:
                    self.puerto_usado += 1
                    continue
                else:
                    print("El servidor RPC no puede ser iniciado")
                    raise


        #Se registra cada funcion
        self.server.register_function(self.do_reporte, 'reporte')
        self.server.register_function(self.do_ayuda, 'ayuda')
        self.server.register_function(self.do_activacion_desactivacion, 'activacion_desactivacion')
        self.server.register_function(self.do_modo_vinculo, 'modo_vinculo')
        self.server.register_function(self.do_modo_efector, 'modo_efector')
        self.server.register_function(self.do_modo_homing, 'modo_homing')
        self.server.register_function(self.do_modo_automatico, 'modo_automatico')

        # Se lanza el servidor
        self.thread = Thread(target=self.run_server)
        self.thread.start()
        print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))



    def run_server(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join()

    def do_reporte(self):
        return self.contorlador.REPORTE()

    def do_ayuda(self):
        return self.contorlador.AYUDA()

    def do_activacion_desactivacion(self, activacion=True):
        return self.contorlador.ACTIVACION_DESACTIVACION(activacion)

    def do_modo_vinculo(self, q1=0, q2=0, q3=0, v1=0, v2=0, v3=0):
        return self.contorlador.MODO_VINCULO(q1, q2, q3, v1, v2, v3)

    def do_modo_efector(self, x=0, y=0, a=0, t=0):
        return self.contorlador.MODO_EFECTOR(x, y, a, t)

    def do_modo_homing(self):
        return self.contorlador.MODO_HOMING()

    def do_modo_automatico(self, numero_archivo=0):
        return self.contorlador.MODO_AUTOMATICO(numero_archivo)