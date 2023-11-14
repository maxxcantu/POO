
class Modo_EF:

    def __init__(self, ROBOT):
        self.descripcion = "Calcula la posición de las articulaciones"
        self.ROBOT = ROBOT

    def __str__(self):
        return self.descripcion

    def realizar(self, x, y, alfa, t):
        cordCartesianas = [x, y, alfa]
        cordCartesianas = ['%.2f' % elem for elem in cordCartesianas]
        self.ROBOT.xyg = [x, y, alfa, t]
        fCart = open("Cartesianas.txt", "a")
        fArt = open("Articuladas.txt", "a")
        fCart.write(str(cordCartesianas) + "\n")
        fCart.close()
        cin_inv = self.ROBOT.ikine(x, y, alfa, self.ROBOT.qr)
        cin_inv = ['%.2f' % elem for elem in cin_inv]
        fArt.write(str(cin_inv) + "\n")
        fArt.close()
        ret = "\n\n>>> Modo efector realizado: \n>>> Las posiciones articulares son: " \
                + "\n>>> " + str(cin_inv) + " <<<\n"
        return ret