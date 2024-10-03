# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:33:53 2024

@author: daniv
"""
import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import serial.tools.list_ports
import serial
import numpy as np
import struct

import threading
import datetime

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import deque

class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        uic.loadUi("lab4 ECG3.ui", self)
        self.puertos_disponibles()
        self.ser = None
        self.connect.clicked.connect(self.conectar)
        self.save.clicked.connect(self.guardar_datos)
        self.load.clicked.connect(self.cargar_y_mostrar_datos)
        
        self.x_todos = deque()  # Almacena todos los puntos en el eje x
        self.y_todos = deque()  # Almacena todos los puntos en el eje y

        self.x = deque(maxlen=500)  # Mantener los últimos 100 puntos en el eje x
        self.y = deque(maxlen=500)  # Mantener los últimos 100 puntos en el eje y

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.grafica.setLayout(layout)

    def puertos_disponibles(self):
        p = serial.tools.list_ports.comports()
        for port in p:
            self.puertos.addItem(port.device)

    def conectar(self):
        estado = self.connect.text()
        self.stop_event_ser = threading.Event()

        if estado == "Conectar":
            com = self.puertos.currentText()
            try:
                self.ser = serial.Serial(com, 115200)
                self.hilo_ser = threading.Thread(target=self.periodic_thread)
                self.hilo_ser.start()
                print("Puerto serial Conectado")
                self.connect.setText("Desconectar")
            except serial.SerialException as e:
                print("Error en el puerto serial: ", e)

        else:
            if self.ser:
                self.ser.close()
                self.hilo_ser.join()
            print("Puerto serial Desconectado")
            self.connect.setText("Conectar")

    def periodic_thread(self):
        try:
            contador = 0
            while not self.stop_event_ser.is_set():
                datos_bytes = self.ser.read(1)
                dato_entero = int.from_bytes(datos_bytes, byteorder='little')
                if dato_entero != 0:
                    # Guardar todos los datos
                    self.x_todos.append(contador)
                    self.y_todos.append(dato_entero)

                    # Guardar los últimos 100 datos para mostrar en la gráfica
                    self.x_mostrar.append(contador)
                    self.y_mostrar.append(dato_entero)
                    contador += 1

                    # Actualizar la gráfica con los últimos 100 puntos
                    self.ax.clear()
                    self.ax.plot(self.x_mostrar, self.y_mostrar, color='blue')  # Cambiar el color aquí
                    self.ax.set_xlabel('Tiempo')
                    self.ax.set_ylabel('Valor')
                    self.ax.set_title('ECG')
                    self.canvas.draw()

        except Exception as e:
            print("Error en el hilo serial: ", e)

    def guardar_datos(self):
        try:
            now = datetime.datetime.now()
            fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
            nombre_persona = self.nombre.text().replace(":", "").replace(" ", "_")
            nombre_archivo = f"{nombre_persona}.txt"
            
            with open(nombre_archivo, 'w') as f:
                f.write(f"Fecha y hora: {fecha_hora}\n")
                f.write(f"Nombre de la persona: {nombre_persona}\n")
                f.write("Datos de la medición:\n")
                for i in range(len(self.x_todos)):
                    f.write(f"{self.x_todos[i]}, {self.y_todos[i]}\n")

            print(f"Datos guardados en {nombre_archivo}")

        except Exception as e:
            print("Error al guardar los datos:", e)

    def cargar_datos(self, nombre_archivo):
        try:
            x = []
            y = []
           
            with open(nombre_archivo, 'r') as f:
                for _ in range(4):
                    next(f)
                
                for line in f:
                    datos = line.strip().split(",")
                    x.append(float(datos[0]))
                    y.append(float(datos[1]))
            return x, y

        except Exception as e:
            print("Error al cargar los datos:", e)
            return None, None

    def cargar_y_mostrar_datos(self):
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if nombre_archivo:
            x, y = self.cargar_datos(nombre_archivo)
            if x and y:
                self.x = x
                self.y = y
                self.ax.clear()
                self.ax.plot(self.x, self.y, color='#ee5ca0')  # Cambiar el color aquí
                self.ax.set_xlabel('Tiempo')
                self.ax.set_ylabel('Valor')
                self.ax.set_title('Datos cargados desde archivo')
                self.canvas.draw()
                print("Datos cargados y mostrados desde", nombre_archivo)
            else:
                print("No se pudieron cargar los datos desde", nombre_archivo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec())
