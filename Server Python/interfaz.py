
import time #Para usar sleep() en 'exit'
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox


class InterfazLocal:

    def __init__(self, controlador):
        self.controlador = controlador
        self.estado_reporte = False

    def realizar(self):
        self.ventana = tk.Tk()
        self.ventana.title("INTERFAZ LOCAL PARA CONTROLAR ROBOT")
        self.ventana.geometry("700x480")
        self.ventana.resizable(width=False, height=False)
        self.ventana.config(bg="gray30")
        self.logo = tk.PhotoImage(file="logo2.png")
        self.imagen = tk.Label(self.ventana, image=self.logo)
        self.imagen.pack(pady=20)

        #Seccion activacion/desactivacion
        self.et_act_des = tk.Label(self.ventana, text="ACTIVACION O DESACTIVACION DEL ROBOT")
        self.et_act_des.pack(fill=tk.X)
        self.et_act_des.config(bg="dim gray", fg="white", font=("Arial",14, "bold"))

        self.act = tk.Button(self.ventana, text="Activacion", command=self.activacion)
        self.act.place(x=133, y=160, width=150, height=30)

        self.des = tk.Button(self.ventana, text="Desactivacion", command=self.desactivacion)
        self.des.place(x=418, y=160, width=150, height=30)

        #Seccion de modos (vinculo, efector, homing y automatico)
        self.et_modos = tk.Label(self.ventana, text="MODOS DE FUNCIONAMIENTO DEL ROBOT")
        self.et_modos.place(y=220, width=700)
        self.et_modos.config(bg="dim gray", fg="white", font=("Arial",14, "bold"))

        self.modo_vinculo = tk.Button(self.ventana, text="Modo Vínculo", command=self.interfazVinculo)
        self.modo_vinculo.place(x=20, y=270, width=150, height=30)

        self.modo_efector = tk.Button(self.ventana, text="Modo Efector", command=self.interfazEfector)
        self.modo_efector.place(x=190, y=270, width=150, height=30)

        self.modo_homing = tk.Button(self.ventana, text="Modo Homing", command=self.modoHoming)
        self.modo_homing.place(x=360, y=270, width=150, height=30)

        self.modo_automatico = tk.Button(self.ventana, text="Modo Automatico", command=self.interfazAutomatico)
        self.modo_automatico.place(x=530, y=270, width=150, height=30)

        #Seccion opciones (ayuda, listado)
        self.et_opc = tk.Label(self.ventana, text="OPCIONES")
        self.et_opc.place(y=330, width=700)
        self.et_opc.config(bg="dim gray", fg="white", font=("Arial", 14, "bold"))

        self.ayuda = tk.Button(self.ventana, text="Ayuda", command=self.Ayuda)
        self.ayuda.place(x=133, y=380, width=150, height=30)

        self.listado = tk.Button(self.ventana, text="Listado", command=self.reporte)
        self.listado.place(x=418, y=380, width=150, height=30)

        #Boton salir
        self.salir = tk.Button(self.ventana, text="Salir", command=self.exit).pack(side=tk.BOTTOM, pady=10)

        self.ventana.mainloop()
        exit(0)

    def interfazVinculo(self):
        #self.vent_vinculo = tk.Tk()
        self.vent_vinculo = tk.Toplevel(self.ventana)
        self.vent_vinculo.title("MODO VINCULO")
        self.vent_vinculo.config(bg="gray30")
        self.vent_vinculo.geometry("410x260")
        self.vent_vinculo.resizable(width=False, height=False)

        self.et_coord = tk.Label(self.vent_vinculo, text="COORDENADAS ARTICULARES")
        self.et_coord.pack(fill=tk.X)
        self.et_coord.config(bg="dim gray", fg="white", font=("Arial", 14, "bold"))

        self.etiq_q1 = tk.Label(self.vent_vinculo, text="q1:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_q1.place(x=0, y=50)
        self.q1 = tk.IntVar()
        self.in_q1 = tk.Entry(self.vent_vinculo, textvariable=self.q1, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_q1.place(x=30, y=50, width=100)

        self.etiq_q2 = tk.Label(self.vent_vinculo, text="q2:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_q2.place(x=140, y=50)
        self.q2 = tk.IntVar()
        self.in_q2 = tk.Entry(self.vent_vinculo, textvariable=self.q2, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_q2.place(x=170, y=50, width=100)

        self.etiq_q3 = tk.Label(self.vent_vinculo, text="q3:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_q3.place(x=280, y=50)
        self.q3 = tk.IntVar()
        self.in_q3 = tk.Entry(self.vent_vinculo, textvariable=self.q3, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_q3.place(x=310, y=50, width=100)

        self.et_vel = tk.Label(self.vent_vinculo, text="VELOCIDADES ARTICULARES")
        self.et_vel.place(y=100, width=410)
        self.et_vel.config(bg="dim gray", fg="white", font=("Arial", 14, "bold"))

        self.etiq_v1 = tk.Label(self.vent_vinculo, text="v1:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_v1.place(x=0, y=150)
        self.v1 = tk.IntVar()
        self.in_v1 = tk.Entry(self.vent_vinculo, textvariable=self.v1, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_v1.place(x=30, y=150, width=100)

        self.etiq_v2 = tk.Label(self.vent_vinculo, text="v2:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_v2.place(x=140, y=150)
        self.v2 = tk.IntVar()
        self.in_v2 = tk.Entry(self.vent_vinculo, textvariable=self.v2, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_v2.place(x=170, y=150, width=100)

        self.etiq_v3 = tk.Label(self.vent_vinculo, text="v3:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_v3.place(x=280, y=150)
        self.v3 = tk.IntVar()
        self.in_v3 = tk.Entry(self.vent_vinculo, textvariable=self.v3, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_v3.place(x=310, y=150, width=100)

        self.ingresar = tk.Button(self.vent_vinculo, text="Ingresar", command=self.modoVinculo)
        self.ingresar.pack(side=tk.BOTTOM, pady=10)

        self.vent_vinculo.mainloop()
        exit(0)

    def interfazEfector(self):
        #self.vent_efector = tk.Tk()
        self.vent_efector = tk.Toplevel(self.ventana)
        self.vent_efector.title("MODO EFECTOR")
        self.vent_efector.config(bg="gray30")
        self.vent_efector.geometry("350x210")
        self.vent_efector.resizable(width=False, height=False)

        self.et_coord_cart = tk.Label(self.vent_efector, text="COORDENADAS CARTESIANAS")
        self.et_coord_cart.pack(fill=tk.X)
        self.et_coord_cart.config(bg="dim gray", fg="white", font=("Arial", 14, "bold"))

        self.etiq_x = tk.Label(self.vent_efector, text="x:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_x.place(x=30, y=50)
        self.x = tk.IntVar()
        self.in_x = tk.Entry(self.vent_efector, textvariable=self.x, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_x.place(x=50, y=50, width=100)

        self.etiq_y = tk.Label(self.vent_efector, text="y:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_y.place(x=180, y=50)
        self.y = tk.IntVar()
        self.in_y = tk.Entry(self.vent_efector, textvariable=self.y, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_y.place(x=200, y=50, width=100)

        self.etiq_alfa = tk.Label(self.vent_efector, text="alfa:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_alfa.place(x=20, y=100)
        self.alfa = tk.IntVar()
        self.in_alfa = tk.Entry(self.vent_efector, textvariable=self.alfa, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_alfa.place(x=60, y=100, width=100)

        self.etiq_t = tk.Label(self.vent_efector, text="t:", font='bold')  # .pack(side=tk.LEFT)
        self.etiq_t.place(x=180, y=100)
        self.t = tk.IntVar()
        self.in_t = tk.Entry(self.vent_efector, textvariable=self.t, justify=tk.RIGHT)  # .pack(side=tk.LEFT, pady=30)
        self.in_t.place(x=200, y=100, width=100)

        self.ingresar2 = tk.Button(self.vent_efector, text="Ingresar", command=self.modoEfector)
        self.ingresar2.pack(side=tk.BOTTOM, pady=10)

        self.vent_efector.mainloop()
        exit(0)

    def interfazAutomatico(self):
        # self.vent_auto = tk.Tk()
        self.vent_auto = tk.Toplevel(self.ventana)
        # self.vent_auto.attributes('-topmost', True)
        self.vent_auto.title("MODO AUTOMATICO")
        self.vent_auto.config(bg="gray30")
        self.vent_auto.geometry("350x190")
        self.vent_auto.resizable(width=False, height=False)


        self.explorar = tk.Button(self.vent_auto, text="Explorar", command=self.buscar_ruta).pack(pady=10)
        self.et_falsa = tk.Label(self.vent_auto, bg='white')
        self.et_falsa.place(x=50, y=60, width=250, height=30)
        self.abrir = tk.Button(self.vent_auto, text="Abrir")
        self.abrir.place(x=135, y=140, width=80)
        # if (self.ruta == " "):
        #     messagebox.showwarning("ABRIR ARCHIVO", "NO HA SELECCIONADO NINGUN ARCHIVO!")
        # con funcion 'lambda' en un 'command' de un boton puede pasar argumentos a la funcion q se invoca

        self.vent_auto.mainloop()
        exit(0)

    def buscar_ruta(self):

        self.ruta = fd.askopenfilename()

        self.entry_ruta = tk.Message(self.vent_auto, text=self.ruta, bg='white', width=230)
        self.entry_ruta.place(x=50, y=60, width=250)
        self.abrir = tk.Button(self.vent_auto, text="Abrir", command=lambda: self.modoAutomatico(self.ruta))
        self.abrir.place(x=135, y=140, width=80)

    def activacion(self):

        print(self.controlador.ACTIVACION_DESACTIVACION(True))
        # controlador.ACTIVACION_DESACTIVACION(True)

    def desactivacion(self):
        print(self.controlador.ACTIVACION_DESACTIVACION(False))

    def modoVinculo(self):
        #los casteo a string para poder imprimirlos, pero al implementarlo en el proyecto tienen q ser int
        self.get_q1 = str(self.in_q1.get())
        self.get_q2 = str(self.in_q2.get())
        self.get_q3 = str(self.in_q3.get())
        self.get_v1 = str(self.in_v1.get())
        self.get_v2 = str(self.in_v2.get())
        self.get_v3 = str(self.in_v3.get())

        print(self.controlador.MODO_VINCULO(int(self.get_q1), int(self.get_q2), int(self.get_q3), int(self.get_v1), int(self.get_v2), int(self.get_v3)))

        self.vent_vinculo.destroy()

    def modoEfector(self):
        #los casteo a string para poder imprimirlos, pero al implementarlo en el proyecto tienen q ser int
        self.get_x = str(self.in_x.get())
        self.get_y = str(self.in_y.get())
        self.get_alfa = str(self.in_alfa.get())
        self.get_t = str(self.in_t.get())

        print(self.controlador.MODO_EFECTOR(int(self.get_x), int(self.get_y), int(self.get_alfa), int(self.get_t)) )

        self.vent_efector.destroy()


    def modoHoming(self):
        print(self.controlador.MODO_HOMING())

    def modoAutomatico(self, ruta):

        if (self.ruta == None):
            messagebox.showwarning("ABRIR ARCHIVO", "NO HA SELECCIONADO NINGUN ARCHIVO!")
        else:
            self.vent_auto.destroy()
            ruta = str(ruta)
            len_ruta = len(ruta)
            len_txt = int(len(".txt"))
            archivo = int(ruta[len_ruta-len_txt-1])

            print(self.controlador.MODO_AUTOMATICO(archivo))

    def Ayuda(self):
        self.vent_ayuda = tk.Toplevel(self.ventana)
        self.vent_ayuda.title("AYUDA")
        self.vent_ayuda.config(bg="gray30")
        self.vent_ayuda.geometry("520x300")
        self.vent_ayuda.resizable(width=False, height=False)

        self.mje_ayuda = "Activación: \tActivar robot\n" + \
                         "Desactivación: \tDesactivar robot\n\n" + \
                         "Modo vínculo: \tIngresar coordenadas articulares (q1, q2, q3) y " \
                                        "\n\t\tvelocidades articulares (v1, v2, v3) de cada articulación\n" + \
                         "Modo efector: \tIngresar coordeanadas cartesianas (x, y) y  " \
                                        "\n\t\torientacion (alfa, t) del efector\n" +  \
                         "Modo homing: \tRegresar el robot a la posición de 'home'\n" + \
                         "Modo automático: \tAbrir archivo de texto con indicaciones predefinidas\n\n" + \
                         "Listado: \t\tSolicitar registro de las tareas realizadas junto " \
                                    "\n\t\tcon la hora y la fecha"


        self.ayuda = tk.Label(self.vent_ayuda, text=self.mje_ayuda, bg="gray30", fg="white", justify=tk.LEFT)#.pack(padx=10, pady=10)
        self.ayuda.place(x=10, y=10)

        self.ok_ayuda = tk.Button(self.vent_ayuda, text="Ok", command=self.vent_ayuda.destroy)
        self.ok_ayuda.place(x=225, y=250, width=70)

        self.vent_ayuda.mainloop()
        exit(0)

    def reporte(self):
        print(self.controlador.REPORTE())
        self.estado_reporte = True

    def exit(self):

        if self.estado_reporte == False:
            pregunta = messagebox.askyesno("SALIR", "Desea obtener el LISTADO antes de salir?")
            if pregunta == True:
                print(self.controlador.REPORTE())
                self.estado_reporte = True
                print(self.controlador.ACTIVACION_DESACTIVACION(False))
                print("\nGracias por utiizar la conexion local, cerrando...")
                time.sleep(3)
                self.ventana.quit()
                exit(0)
            else:
                print(self.controlador.ACTIVACION_DESACTIVACION(False))
                print("\nGracias por utiizar la conexion local, cerrando...")
                time.sleep(3)
                self.ventana.quit()
                exit(0)
        else:
            print(self.controlador.ACTIVACION_DESACTIVACION(False))
            print("\nGracias por utiizar la conexion local, cerrando...")
            time.sleep(3)
            self.ventana.quit()
            exit(0)
        # return self.comandos
        # self.ventana.quit()

        # self.vent_exit = tk.Toplevel(self.ventana)
        # self.vent_exit.title("EXIT")
        # self.vent_exit.config(bg="gray30")
        # self.vent_exit.geometry("300x80")
        # self.vent_exit.resizable(width=False, height=False)
        #
        #
        # self.mje_exit = "Gracias por utilizar la\n conexión local"
        #
        # self.et_exit = tk.Label(self.vent_exit, text=self.mje_exit, bg="gray30", fg="white")
        # self.et_exit.config(font=("Arial",18, "bold"))
        # self.et_exit.pack()
        # # self.et_exit.place(x=10, y=10)
        #
        # self.vent_exit.mainloop()
        #
        # time.sleep(5)
        #
        # self.vent_exit.destroy()
        #
        #
        # self.ventana.quit()




