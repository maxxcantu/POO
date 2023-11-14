
class Modo_Vinculo:
    def __init__(self, ROBOT):
        self.descripcion = 'Recibe ordenes de coordenadas articulares'
        self.ROBOT = ROBOT

    def __str__(self):
        return self.descripcion

    def realizar(self, q1, q2, q3):
        pos = self.ROBOT.fkine(q1, q2, q3)
        pos = ['%.2f' % elem for elem in pos]
        q = [q1, q2, q3]
        q = ['%.2f' % elem for elem in q]
        fCart = open("Cartesianas.txt", "a")
        fCart.write(str(pos) + "\n")
        fCart.close()
        fArt = open("Articuladas.txt", "a")
        fArt.write(str(q) + "\n")
        fArt.close()
        ret = "\n\n>>> Modo vinculo realizado: \n>>> La posición del efector final es: " + \
              "\n>>> " + str(pos) + " <<<\n"
        return ret