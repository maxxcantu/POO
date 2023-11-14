
import robot
import reporte
import time

import modo_efector
import modo_homing
import modo_vinculo
import modo_automatico

class controlRobot:
    ROBOT = robot.Robot("Tony")
    reporte = reporte.Reporte()

    def REPORTE(self):
        retorno_reporte = self.reporte.get_comandos()
        return retorno_reporte

    def AYUDA(self):
        retorno_ayuda = """\nLos comandos para cada instrucción son los siguientes:
                    \n CONEXION:\tC \n DESCONEXION:\tD \n LISTADO:\tL \n AYUDA:\t\tA
                    \n ACTIVACION:\tAc \n DESACTIVACION:\tDe \n\n MODO VINCULO:\tMv \n MODO EFECTOR:\tMe \n MODO HOMING:\tMh \n MODO AUTOMATICO:\tMa 
                    \n\nFormato Mv: MVq1,q2,q3,v1,v2,v3 
                    \nFormato Me: MEx,y,alfa,t
                    \nFormato Ma: MAi
                    \n\nAl ingresar múltiples instrucciones, separar mensajes por '-' """
        return retorno_ayuda

    def ACTIVACION_DESACTIVACION(self, activacion):
        if activacion:
            if not self.ROBOT.estado:
                self.ROBOT.activar()
                retorno_activacion = "\n\n>>> Robot activado <<<"
                self.reporte.set_comandos("Activación")
                return retorno_activacion
            else:
                retorno_activacion = "\n\n>>> El robot ya está activado <<<"
                return retorno_activacion
        else:
            if self.ROBOT.estado:
                self.ROBOT.desactivar()
                retorno_desactivacion = "\n\n>>> Robot desactivado <<<"
                self.reporte.set_comandos("Desactivacion")
                return retorno_desactivacion
            else:
                retorno_desactivacion = "\n\n>>> El robot ya estaba desactivado <<<"
                return retorno_desactivacion

    def MODO_VINCULO(self, q1, q2, q3, v1, v2, v3):
        if self.ROBOT.estado:
            qt1 = " q1=" + str(q1) + " q2=" + str(q2) + " q3=" + str(q3) \
                + " v1=" + str(v1) + " v2=" + str(v2) + " v3=" + str(v3)
            self.reporte.set_comandos(("Modo vinculo" + qt1))
            vinculo = modo_vinculo.Modo_Vinculo(self.ROBOT)
            vector_modo_vinculo = vinculo.realizar(q1, q2, q3)
        else:
            vector_modo_vinculo = "\n\n>>> El robot no está activado <<<"

        return str(vector_modo_vinculo)

    def MODO_EFECTOR(self, x, y, a, t):
        if self.ROBOT.estado:
            xt1 = " x=" + str(x) + " y=" + str(y) + " a=" + str(a) + " t=" + str(t)
            self.reporte.set_comandos(("Modo efector" + xt1))
            efector_final = modo_efector.Modo_EF(self.ROBOT)
            vector_modo_efector = efector_final.realizar(x, y, a, t)
        else:
            vector_modo_efector = "\n\n>>> El robot no está activado <<<"

        return vector_modo_efector

    def MODO_HOMING(self):
        if self.ROBOT.estado:
            self.reporte.set_comandos("Modo homing")
            homing = modo_homing.Modo_Homing(self.ROBOT)
            vector_modo_homing = homing.realizar()
        else:
            vector_modo_homing = "\n\n>>> El robot no está activado <<<"

        return vector_modo_homing

    def MODO_AUTOMATICO(self, archivo):
        archivo = int(archivo)
        if self.ROBOT.estado:
            self.reporte.set_comandos("Modo automatico desde archivo: " + "modo_auto_" + str(archivo) + ".txt")
            automatico = modo_automatico.Modo_Automatico(archivo, self.ROBOT)
            vector_modo_automatico = automatico.realizar()
        else:
            vector_modo_automatico = "\n\n>>> El robot no está activado <<<"

        return vector_modo_automatico
