
class Modo_Homing:
    def __init__(self, ROBOT):
        self.descripcion = "Realiza el homing"
        self.ROBOT = ROBOT

    def _str_(self):
        return "metodoManual".format(self.descripcion)

    def realizar(self):
        fCart = open("Cartesianas.txt", "a")
        fArt = open("Articuladas.txt", "a")
        fArt.write("[0.00 0.00 0.00]\n")
        cart = self.ROBOT.fkine(0, 0, 0)
        cart = ['%.2f' % elem for elem in cart]
        fCart.write(str(cart)+"\n")
        fCart.close()
        fArt.close()
        return "\n\n>>> Homing realizado <<<\n"