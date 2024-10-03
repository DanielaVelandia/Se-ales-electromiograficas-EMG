
### SEÑALES ELECTROMIOGRÁFICAS EMG

La electromiografía (EMG) es una técnica de diagnóstico que permite evaluar la actividad eléctrica de los músculos y las neuronas que los controlan. Existen dos tipos de electrodos utilizados en este procedimiento: los de superficie y los intramusculares o de aguja. En esta práctica de laboratorio, se emplearán electrodos de superficie, los cuales son esenciales para registrar las señales eléctricas de los músculos sin necesidad de invadir el cuerpo del paciente.
Para capturar las señales mioeléctricas, se utilizan dos electrodos activos y un electrodo de referencia o tierra. Los electrodos de superficie se colocan sobre la piel, específicamente sobre el músculo a estudiar, mientras que el electrodo de tierra se coloca en una parte del cuerpo que no tenga actividad eléctrica significativa. La señal EMG es el resultado de la diferencia entre las señales captadas por los electrodos activos.
Para llevar a cabo el laboratorio 3 de procesamiento digital de señales, se siguió un procedimiento detallado que se explicará paso a paso a continuación:

**1.	Preparación del Sujeto y Adquisición de la Señal EMG:**

En primer lugar, es esencial colocar los electrodos de superficie sobre el músculo a analizar, asegurando una buena adherencia con gel conductor para optimizar la captación de señales. Los electrodos se conectaron al AD8232, un circuito integrado diseñado específicamente para la adquisición y procesamiento de señales biopotenciales, como las que se generan en un electrocardiograma (ECG). Este circuito es capaz de extraer, amplificar y filtrar señales biopotenciales de baja amplitud en entornos con ruido. El AD8232, encargado de procesar las señales biopotenciales, se conectará de forma serial a una placa STM. Con la ayuda de programación, se diseñó una interfaz gráfica que permite visualizar en tiempo real la actividad eléctrica de los músculos y almacenar los datos adquiridos para su análisis posterior. 

![image](https://github.com/user-attachments/assets/9c6e9e05-feac-4783-9efa-23156c13ffe1)

Para esta práctica, se seleccionaron dos músculos: el extensor de los dedos y el flexor ulnar del carpo, que serán objeto de estudio. El electrodo de tierra se ubicó en el codo del brazo, una zona eléctricamente inactiva, con el objetivo de estabilizar la señal y minimizar posibles interferencias, se le solicito al sujeto de prueba que realizara contracción muscular con ayuda de una pelota hasta llegar a la fática muscular.

 ![image](https://github.com/user-attachments/assets/c2c16f43-0c97-4656-9e5e-dec6cf329bcb)

Un aspecto clave en esta práctica es la frecuencia de muestreo de la electromiografía (EMG) para los músculos del antebrazo, ya que influye directamente en la calidad y precisión de los datos recolectados. Se recomienda que la frecuencia de muestreo oscile entre 1000 Hz y 2000 Hz para capturar adecuadamente las señales eléctricas generadas por los músculos.

 ![image](https://github.com/user-attachments/assets/3cc7b8f3-5176-40bc-8a40-8d82140cacd9)

> **Ejes de la Gráfica:**

> > **-El eje horizontal (Tiempo [s]):** Este eje muestra cómo cambia la actividad eléctrica del músculo a lo largo del tiempo, permitiendo observar la secuencia de eventos eléctricos durante la contracción y relajación muscular.

> > **-El eje vertical (Amplitud [mV]):** representa la amplitud de la señal eléctrica registrada. Esta amplitud refleja la magnitud de los potenciales de acción generados por las unidades motoras en el músculo.

**2.	 Filtrado de la Señal:**

Para el filtrado de la señal, se utilizó una combinación de un filtro pasa bajo y un filtro pasa alto, formando un filtro pasa banda. El filtro pasa bajo se empleó para eliminar las frecuencias altas no deseadas, mientras que el filtro pasa alto se utilizó para suprimir las componentes de baja frecuencia. Esta configuración permite que solo pase un rango específico de frecuencias, mientras atenúa las frecuencias por debajo y por encima de ese rango, asegurando que solo se capturen las señales relevantes para el análisis electromiográfico.
Con base en lo anterior, se diseñó un filtro pasa-bajo con una frecuencia de corte de 10 Hz y una atenuación de 60 Hz. Luego, se normalizó la expresión convirtiendo Hz a rad/s, se definió la amplitud en dB y se evaluó el orden del filtro, obteniendo un filtro de cuarto orden. Posteriormente, se definió el polinomio característico del filtro Butterworth.
El filtro pasa-bajo diseñado se transformó en un filtro pasa-banda con frecuencias de corte de 10 Hz y 500 Hz, reemplazando los valores correspondientes en la ecuación característica para obtener el filtro final.

> **Diseño del filtro:**
> > **•	Frecuencia de corte baja (fL):** 10 Hz

> > **•	Frecuencia de corte alta (fH):** 500 Hz

> > **•	Frecuencia de muestreo (fs):** 1000 Hz

> > **•	Atenuación fuera de la banda:** 60 Hz

> > **•	Orden del filtro:** Butterworth orden 4

![image](https://github.com/user-attachments/assets/bf2fe775-32f3-4985-8e01-f90c2ba7ad86)

**3.	 Aventanamiento:**

Para realizar el aventanamiento de la señal, se empleó la técnica de la ventana de Hamming, esta es una herramienta utilizada en el procesamiento de señales para mejorar la calidad del análisis espectral y minimizar efectos no deseados, como las discontinuidades en los bordes de la señal.
Es importante entender que una ventana es una función matemática que se aplica a una señal para limitar su duración y facilitar su análisis en el dominio de la frecuencia. Al multiplicar la señal por una función ventana, se selecciona solo una parte de la señal para su análisis, lo que ayuda a suavizar las transiciones en los extremos, evitando discontinuidades al inicio y al final del segmento. Esto permite obtener un análisis espectral más preciso.
Una vez que la señal ha sido suavizada con la ventana de Hamming, se aplicó la Transformada de Fourier para transformar la señal del dominio del tiempo al dominio de la frecuencia. La Transformada de Fourier permite calcular eficientemente los coeficientes de frecuencia, proporcionando el espectro correspondiente.
Para realizar el aventanamiento, se consideró una frecuencia de corte de 1000 Hz, lo que garantiza que las señales de interés sean capturadas adecuadamente sin perder información relevante. El aventanamiento se llevó a cabo cada 250 ms, lo que significa que se procesan segmentos de la señal en intervalos de tiempo de un cuarto de segundo. Se realizaron un total de 24 ventanas correspondientes a las 24 repeticiones efectuadas durante el ejercicio, hasta alcanzar el punto de fatiga muscular.

![image](https://github.com/user-attachments/assets/8b51b90d-6029-418b-83a1-7fef0c428474)

![image](https://github.com/user-attachments/assets/5b89f0cc-b051-4f47-a1d8-c56e9aecd68b)

 
**4.	 Análisis Espectral:**

Cuando se le pide al sujeto de prueba que realice una contracción muscular sostenida, la amplitud de la señal EMG tiende a aumentar inicialmente debido al reclutamiento de más unidades motoras para mantener la fuerza requerida. Sin embargo, a medida que el músculo experimenta fatiga, la amplitud de la señal comienza a disminuir gradualmente. Esta reducción en la amplitud se debe a la incapacidad del músculo para mantener el mismo nivel de activación, lo que refleja una disminución en la fuerza generada por las fibras musculares. Este fenómeno es una indicación clara de la fatiga muscular, que puede ser observada a través de la gráfica.

![image](https://github.com/user-attachments/assets/c6385193-8794-4152-8602-a54f4db89416)

 > **Ejes de la Gráfica:**

> > **-El eje horizontal (Ventanas):** Números de ventanas.
> > 
> > **-El eje vertical (Frecuencia [Hz]):** Frecuencias medianas medidas con respecto a las ventanas.

• La frecuencia mediana es un parámetro estadístico que se utiliza para describir la distribución de las frecuencias presentes en la señal EMG. Este valor proporciona una medida que indica el punto medio de las frecuencias, separando la mitad superior de la mitad inferior de los datos.

• la frecuencia dominante en una señal de electromiografía (EMG) se refiere al rango de frecuencias donde se concentra la mayor parte de la energía de la señal registrada. Esta frecuencia es crucial para entender cómo se comporta la actividad eléctrica del músculo durante la contracción.

• La frecuencia media, se utiliza para describir el promedio de todas las frecuencias presentes en una señal durante un período específico. Este valor ofrece una visión general del comportamiento frecuencial de la señal a lo largo del tiempo.

• La desviación estándar es una medida que indica la dispersión o variabilidad de un conjunto de datos con respecto a su media. En el contexto de la señal EMG, una desviación estándar baja sugiere que las frecuencias están agrupadas cerca de la media, mientras que una desviación estándar alta indica una mayor variabilidad en las frecuencias registradas.

> **Datos estadisticos obtenidos por cada ventana:**
> > **-Ventana 1:** Frecuencia Mediana: 148.00 Hz, Frecuencia Dominante: 124.00 Hz, Frecuencia Media: 164.99 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 2:** Frecuencia Mediana: 220.00 Hz, Frecuencia Dominante: 220.00 Hz, Frecuencia Media: 222.11 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 3:** Frecuencia Mediana: 164.00 Hz, Frecuencia Dominante: 168.00 Hz, Frecuencia Media: 164.57 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 4:** Frecuencia Mediana: 152.00 Hz, Frecuencia Dominante: 152.00 Hz, Frecuencia Media: 174.34 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 5:** Frecuencia Mediana: 148.00 Hz, Frecuencia Dominante: 112.00 Hz, Frecuencia Media: 182.24 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 6:** Frecuencia Mediana: 184.00 Hz, Frecuencia Dominante: 104.00 Hz, Frecuencia Media: 191.83 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 7:** Frecuencia Mediana: 144.00 Hz, Frecuencia Dominante: 140.00 Hz, Frecuencia Media: 177.40 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 8:** Frecuencia Mediana: 184.00 Hz, Frecuencia Dominante: 148.00 Hz, Frecuencia Media: 194.90 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 9:** Frecuencia Mediana: 160.00 Hz, Frecuencia Dominante: 156.00 Hz, Frecuencia Media: 195.25 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 10:** Frecuencia Mediana: 192.00 Hz, Frecuencia Dominante: 188.00 Hz, Frecuencia Media: 202.92 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 11:** Frecuencia Mediana: 240.00 Hz, Frecuencia Dominante: 244.00 Hz, Frecuencia Media: 216.03 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 12:** Frecuencia Mediana: 220.00 Hz, Frecuencia Dominante: 208.00 Hz, Frecuencia Media: 230.65 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 13:** Frecuencia Mediana: 220.00 Hz, Frecuencia Dominante: 252.00 Hz, Frecuencia Media: 217.40 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 14:** Frecuencia Mediana: 200.00 Hz, Frecuencia Dominante: 128.00 Hz, Frecuencia Media: 215.17 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 15:** Frecuencia Mediana: 208.00 Hz, Frecuencia Dominante: 204.00 Hz, Frecuencia Media: 208.01 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 16:** Frecuencia Mediana: 200.00 Hz, Frecuencia Dominante: 304.00 Hz, Frecuencia Media: 210.53 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 17:** Frecuencia Mediana: 212.00 Hz, Frecuencia Dominante: 184.00 Hz, Frecuencia Media: 221.21 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 18:** Frecuencia Mediana: 216.00 Hz, Frecuencia Dominante: 216.00 Hz, Frecuencia Media: 213.18 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 19:** Frecuencia Mediana: 232.00 Hz, Frecuencia Dominante: 248.00 Hz, Frecuencia Media: 217.16 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 20:** Frecuencia Mediana: 216.00 Hz, Frecuencia Dominante: 220.00 Hz, Frecuencia Media: 217.40 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 21:** Frecuencia Mediana: 164.00 Hz, Frecuencia Dominante: 132.00 Hz, Frecuencia Media: 177.50 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 22:** Frecuencia Mediana: 192.00 Hz, Frecuencia Dominante: 108.00 Hz, Frecuencia Media: 189.78 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 23:** Frecuencia Mediana: 152.00 Hz, Frecuencia Dominante: 136.00 Hz, Frecuencia Media: 173.11 Hz, Desviación Estándar: 144.91 Hz
> > 
> > **-Ventana 24:** Frecuencia Mediana: 120.00 Hz, Frecuencia Dominante: 116.00 Hz, Frecuencia Media: 159.53 Hz, Desviación Estándar: 144.91 Hz

![image](https://github.com/user-attachments/assets/a753d986-ef46-498e-a475-bfe3ce36cdf6)

> **Teniendo en cuenta todas las ventanas:**

> > **-Frecuencia dominante:** 154.00 Hz

> > **-Desviación estándar de las frecuencias medianas:** 32.19 Hz

> > **-Frecuencia media:** 187.00 Hz

![image](https://github.com/user-attachments/assets/5d7e6cf8-72bc-480c-aabe-ad654222c86f)

> **Ejes de la Gráfica:**
> > **-El eje horizontal (Frecuencia [Hz]):** Diferentes frecuencias presentes en la señal.

> > **-El eje vertical (Potencia [dB]):** cantidad de potencia asociada con cada frecuencia.

 ###### Valor p de la prueba de hipótesis: 0.4111
Al aplicar la prueba de hipótesis en el análisis del código, se obtuvo un valor p de 0.4111. Esto sugiere que los cambios observados en las señales EMG durante las contracciones hasta la fatiga no son estadísticamente significativos. Dado que el valor p de 0.4111 es mayor que el nivel de significancia comúnmente utilizado (0.05), no se rechaza la hipótesis nula. Esto indica que no hay suficiente evidencia estadística para afirmar que la fatiga muscular tiene un efecto significativo sobre la frecuencia mediana de las señales EMG. En consecuencia, podría inferirse que el protocolo utilizado no generó un efecto notable sobre la actividad eléctrica del músculo.

### INSTRUCCIONES 
Este código está diseñado para ser utilizado en la plataforma Spyder. Para ejecutarlo correctamente, sigue estos pasos:

**1.	Instalación de librerías:** Asegúrate de instalar las librerías necesarias en la consola usando los siguientes comandos:

>	 pip install pyqt5-tools

> pip install numpy

>	 pip install matplotlib

