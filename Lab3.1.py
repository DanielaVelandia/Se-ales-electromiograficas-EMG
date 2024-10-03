# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:55:13 2024

@author: daniv
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, get_window
from scipy.fftpack import fft
from scipy.stats import ttest_rel

# Cargar datos
datos = np.loadtxt('señal.txt', delimiter=',')
tiempo = datos[:, 0]
emg = datos[:, 1]

# Graficar la señal EMG original
plt.figure(figsize=(10, 6))
plt.plot(tiempo, emg, label='Señal EMG', color='#ee5ca5')
plt.title('Señal EMG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.legend()
plt.grid()
plt.show()

# Parámetros del filtro
f_L = 10   
f_H = 500  
f_s = 1000 
n = 4      


# Filtro pasabandas
omega_L = 2 * np.pi * f_L  
omega_H = 2 * np.pi * f_H  
omega_0 = np.sqrt(omega_L * omega_H)
delta_omega = omega_H - omega_L
Q = omega_0 / delta_omega  
T = 1 / f_s
alpha = np.sin(omega_0 * T) / (2 * Q)

b0 = alpha
b1 = 0
b2 = -alpha
a0 = 1 + alpha
a1 = -2 * np.cos(omega_0 * T)
a2 = 1 - alpha

b = [b0/a0, b1/a0, b2/a0]
a = [1, a1/a0, a2/a0]

# Filtrar la señal EMG
def filter_signal(emg, b, a):
    n = len(emg)
    y = np.zeros(n)
    for i in range(n):
        if i == 0:
            y[i] = b[0] * emg[i]
        elif i == 1:
            y[i] = b[0] * emg[i] + b[1] * emg[i - 1] - a[1] * y[i - 1]
        else:
            y[i] = (b[0] * emg[i] + b[1] * emg[i - 1] + b[2] * emg[i - 2] - 
                     a[1] * y[i - 1] - a[2] * y[i - 2])
    return y

emg_filtrada = filter_signal(emg, b, a)

# Graficar la señal EMG filtrada
plt.figure(figsize=(10, 6))
plt.plot(tiempo, emg_filtrada, label='Señal EMG Filtrada', color='#bd5cee')
plt.title('Señal EMG Filtrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.legend()
plt.grid()
plt.show()

def calc_frecuencia_mediana(frecuencia, potencia):
    potencia_acumulada = np.cumsum(potencia)
    potencia_total = potencia_acumulada[-1]
    mediana_idx = np.where(potencia_acumulada >= potencia_total / 2)[0][0]
    return frecuencia[mediana_idx]

# Aventanamiento
fs = 1000 
ventana_tamaño = 250  # ms
ventana_tamaño = int(ventana_tamaño * fs / 1000)  # Convertir a muestras

num_ventanas = len(emg_filtrada) // ventana_tamaño

plt.figure(figsize=(12, 8))

# Graficar todas las ventanas
for i in range(num_ventanas):
    inicio = i * ventana_tamaño
    fin = inicio + ventana_tamaño
    ventana_emg = emg_filtrada[inicio:fin]
    
    ventana_hamming = np.hamming(len(ventana_emg))
    ventana_emg_ventaneada = ventana_emg * ventana_hamming

    plt.plot(tiempo[inicio:fin], ventana_emg_ventaneada, label=f'Ventana {i + 1}' if i % 4 == 0 else "", alpha=0.6) 

plt.title('Ventanas de la Señal EMG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.grid()
plt.legend(loc='upper right')
plt.show()

# Análisis espectral
frecuencias_medianas = []
frecuencias_dominantes = []
frecuencias_media = []
desviaciones_estandar = []
convoluciones = []  # Lista para almacenar las señales convolucionadas

for i in range(num_ventanas):
    inicio = i * ventana_tamaño
    fin = inicio + ventana_tamaño
    ventana_emg = emg_filtrada[inicio:fin]
    
    # Ventana de Hamming
    ventana_hamming = np.hamming(len(ventana_emg))
    ventana_emg_ventaneada = ventana_emg * ventana_hamming
    
    # Convolución
    convolucion = np.convolve(ventana_emg_ventaneada, ventana_hamming, mode='same')
    convoluciones.append(convolucion)
    
    # FFT
    fft_ventana = fft(ventana_emg_ventaneada)
    potencia_ventana = np.abs(fft_ventana[:len(ventana_emg)//2])**2
    frecuencia_ventana = np.fft.fftfreq(len(ventana_emg), d=1/fs)[:len(ventana_emg)//2]

    frecuencia_mediana = calc_frecuencia_mediana(frecuencia_ventana, potencia_ventana)
    frecuencias_medianas.append(frecuencia_mediana)

    # Frecuencia Dominante
    frecuencia_dominante = frecuencia_ventana[np.argmax(potencia_ventana)]
    frecuencias_dominantes.append(frecuencia_dominante)

    # Frecuencia Media
    frecuencia_media = np.sum(frecuencia_ventana * potencia_ventana) / np.sum(potencia_ventana)
    frecuencias_media.append(frecuencia_media)

    # Desviación Estándar
    desviacion_estandar = np.std(frecuencia_ventana, ddof=1)
    desviaciones_estandar.append(desviacion_estandar)

    print(f'Ventana {i+1}: Frecuencia Mediana: {frecuencia_mediana:.2f} Hz, '
          f'Frecuencia Dominante: {frecuencia_dominante:.2f} Hz, '
          f'Frecuencia Media: {frecuencia_media:.2f} Hz, '
          f'Desviación Estándar: {desviacion_estandar:.2f} Hz')

# Graficar las frecuencias calculadas
plt.figure(figsize=(10, 6))
plt.plot(np.arange(num_ventanas), frecuencias_medianas, label='Frecuencia Mediana', color='#f24e7b')
plt.plot(np.arange(num_ventanas), frecuencias_dominantes, label='Frecuencia Dominante', color='#7dbe50')
plt.plot(np.arange(num_ventanas), frecuencias_media, label='Frecuencia Media', color='#5cc8ee')
plt.title('Análisis Espectral por Ventana')
plt.xlabel('Ventanas')
plt.ylabel('Frecuencia [Hz]')
plt.legend()
plt.grid()
plt.show()

# Graficar todas las convoluciones
plt.figure(figsize=(12, 8))

# Configuración de colores para cada ventana
colores = plt.cm.viridis(np.linspace(0, 1, num_ventanas))

for i in range(num_ventanas):
    inicio = i * ventana_tamaño
    fin = inicio + ventana_tamaño
    plt.plot(tiempo[inicio:fin], convoluciones[i], color=colores[i], alpha=0.6, label=f'Convolución Ventana {i + 1}')

plt.title('Convoluciones de cada Ventana de la Señal EMG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.grid()
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='small')  # Ajustar la leyenda
plt.tight_layout()
plt.show()

# Prueba de hipótesis
frecuencia_mediana_antes = frecuencias_medianas[:num_ventanas//2]
frecuencia_mediana_despues = frecuencias_medianas[num_ventanas//2:]

t_stat, p_val = ttest_rel(frecuencia_mediana_antes, frecuencia_mediana_despues)
print(f'Valor p de la prueba de hipótesis: {p_val:.4f}')

# Análisis espectral señal completa
n = len(emg_filtrada)  
frecuencia = np.fft.fftfreq(n, d=1/fs)  
frecuencia = frecuencia[:n // 2]

fft_emg = fft(emg_filtrada)
potencia = np.abs(fft_emg[:n // 2]) ** 2 

plt.figure(figsize=(10, 6))
plt.plot(frecuencia, potencia, label='Espectro de la señal EMG', color='#5cc8ee')
plt.title('Espectro de la Señal EMG Filtrada')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Potencia')
plt.legend()
plt.grid()
plt.show()

frecuencia_dominante = frecuencia[np.argmax(potencia)]
desviacion_estandar_frecuencias = np.std(frecuencias_medianas)
frecuencia_media = np.mean(frecuencias_medianas)

print(f'Frecuencia dominante: {frecuencia_dominante:.2f} Hz')
print(f'Desviación estándar de las frecuencias medianas: {desviacion_estandar_frecuencias:.2f} Hz')
print(f'Frecuencia media: {frecuencia_media:.2f} Hz')

