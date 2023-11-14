import numpy as np
import math
from time import time

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.l1 = 1
        self.l2 = 1
        self.l3 = 1
        self.qr = [0, 0, 0]
        self.xyg = [0, 0, 0, 0]
        self.start_time = time()
        self.estado = 0

    def ikine(self, x, y, gama, qant):
        self.xyg[0] = x
        self.xyg[1] = y
        self.xyg[2] = gama
        q1 = []
        q2 = []
        xm = x - np.cos(gama)
        ym = y - np.sin(gama)
        r = np.power(xm, 2) + np.power(ym, 2)
        r = np.sqrt(r)
        alfa = (1 + np.power(r, 2) - 1) / (2 * r)
        alfa = np.arccos(alfa)
        beta = np.arctan2(ym, xm)
        # calculo de q1
        q = beta - alfa
        q1.append(q)
        q = beta + alfa
        q2.append(q)
        # calcula de q2
        fi = (2 - np.power(r, 2)) / 2
        fi = np.arccos(fi)
        q = math.pi - fi
        q1.append(q)
        q = fi - math.pi
        q2.append(q)
        # calculo de q3
        q = gama - q1[0] - q1[1]
        q1.append(q)
        q = gama - q2[0] - q2[1]
        q2.append(q)
        # seleccion mejor solucion:
        j = 0
        sum1 = 0
        sum2 = 0
        for i in qant:
            sum1 = sum1+abs(i-q1[j])
            sum2 = sum2+abs(i-q2[j])
        if sum1 > sum2:
            self.qr = q1
            return q1
        else:
            self.qr = q2
            return q2   

    def tiempo_usado(self):
        t = time()-self.start_time
        return t

    def tiempo_inicial(self):
        self.start_time = time()

    def activar(self):
        self.estado = 1

    def desactivar(self):
        self.estado = 0
  
    def fkine(self, q1, q2, q3):
        self.qr[0] = q1
        self.qr[1] = q2
        self.qr[2] = q3
        T = []
        T.append(math.cos(q1 + q2 + q3) + math.cos(q1 + q2) + math.cos(q1))
        T.append(math.sin(q1 + q2 + q3) + math.sin(q1 + q2) + math.sin(q1))
        T.append(q1+q2+q3)
        self.xyg = T
        return T

    def vel(self, q1, q2, q3, q1p, q2p, q3p):
        vx = -math.sin(q1 + q2 + q3) * q1p * q2p * q3p + math.cos(q1 + q2 + q3) * q1p * q2p * q3p
        vy = -math.cos(q1 + q2 + q3) * q1p * q2p * q3p - math.sin(q1 + q2 + q3) * q1p * q2p * q3p
        v = math.sqrt(vx * 2 + vy * 2)
        return v

    def __del__(self):
        return 0