import modo_efector
import modo_vinculo
import modo_homing

class Modo_Automatico:

    def __init__(self, archivo, ROBOT):
        self.descripcion = "Ejecuta instrucciones almacenadas en un determinado archivo"
        self.archivo = archivo
        self.ROBOT = ROBOT
        self.modo_v = modo_vinculo.Modo_Vinculo(self.ROBOT)
        self.modo_e = modo_efector.Modo_EF(self.ROBOT)
        self.modo_h = modo_homing.Modo_Homing(self.ROBOT)

    def _str_(self):
        return self.descripcion

    def realizar(self):
        vector_ma = ""
        ma_archivo = "modo_auto_" + str(self.archivo) + ".txt"
        print("\n>>> Se realizarán las instrucciones del archivo: " + ma_archivo )
        file = open(ma_archivo, "r")

        for order in file.readlines():
            if order[0] == "M" or order[0] == "m":
                if order[1] == "V" or order[1] == "v":
                    vector_ma = vector_ma + "\n" + self.do_modo_v(float(order[2]), float(order[3]), float(order[4]))
                if order[1] == "E" or order[1] == "e":
                    vector_ma = vector_ma + "\n" + self.do_modo_e(float(order[2]), float(order[3]), float(order[4]), float(order[5]))
                if order[1] == "H" or order[1] == "h":
                    vector_ma = vector_ma + "\n" + self.do_modo_h()
        file.close()
        return vector_ma

    def do_modo_v(self, q1, q2, q3):
        vector_modo_v = self.modo_v.realizar(q1, q2, q3)
        return vector_modo_v

    def do_modo_e(self, x, y, a, t):
        vector_modo_e = self.modo_e.realizar(x, y, a, t)
        return vector_modo_e

    def do_modo_h(self):
        vector_modo_h = self.modo_h.realizar()
        return vector_modo_h

