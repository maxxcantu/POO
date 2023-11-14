import time
import numpy as np

class Reporte:
    def __init__(self):
        tiempo = time.ctime()
        self.reporte = "\n\nReporte: \n"
        self.reporte = self.reporte + tiempo + " Inicialización del servidor \n"
        self.tinicial = time.time()

    def set_comandos(self, comando):
        tiempo = time.ctime()
        self.reporte = self.reporte + tiempo + " " + comando + "\n"
    
    def get_comandos(self):
        dif = round((time.time() - self.tinicial),2)
        dif = str(dif)
        return self.reporte + "Duración del servidor: " + dif + " segundos\n"

    def __del__(self):
        return 0
