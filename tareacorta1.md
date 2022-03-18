# Tarea Corta #1

## Instituto Tecnológico de Costa Rica

### Curso de Redes

### Analizador de espectros simple para audio

Integrantes:

David Umaña Blanco - 2016175133

Francisco Mata Blanco - 2016106889

Andrés Ramirez Ortega - 2018172107


 <font size="4"> 

# 1. Introducción
Un analizador de espectro es un instrumento que permite visualizar en una pantalla los componentes espectrales en un espectro de frecuencias de las señales presentes en la entrada. Esta señal puede ser de cualquier tipo de ondas, como eléctricas, acústicas u ópticas. El análisis se realiza en la acción de descomponer algo complejo en partes simples o identificar en ese algo complejo las partes más simples que lo forman. El proceso que cuantifique las diversas intensidades de cada frecuencia se llama análisis espectral.

Matemáticamente el análisis espectral está relacionado con la transformada de Fourier. Ese análisis puede llevarse a cabo para pequeños intervalos de tiempo, o menos frecuentemente para intervalos largos, o incluso puede realizarse el análisis espectral de una función determinada. El proposito de esta tarea corta es implementar la transformada de Fourier para hacer una descomposición espectral de los formantes de una onda o señal oscilatoria. Así mismo graficar señales de audio en el dominio del tiempo y dominio de frecuencia, también extraer armónicos específicos para generar tonos de audio, parte de la solución es crear una aplicación llamada Autrum, que tendrá dos partes: Un Analizador que toma señales de audio streaming (captura de micrófono) o batch (archivos WAV), y un Reproductor que toma archivos con extensión .atm y puede reproducir el audio al mismo tiempo que los gráficos en dominio del tiempo y dominio de frecuencia, el usuario podrá detener, cancelar y resumir la reproducción en cualquier momento y realizar una exploración de los gráficos (zoom in / zoom out).


# 2. Marco Teórico
## 2.1 Comunicación de Datos

Mediante la variación de algunas propiedades físicas, como el voltaje o la corriente, se da la posibilidad de transmitir información a través de los cables como medio. El valor del voltaje o corriente que tengamos se puede representar como una función simple del tiempo, f(t), y así de esta forma se puede modelar el comportamiento de la señal para ser analizada matemáticamente. 

### 2.1.1 Análisis de Fourier
En el siglo XIX el matemático francés Jean-Baptiste Fourier probó que cualquier función periódica de comportamiento razonable, g(t) con un periodo T, se puede construir sumando una cantidad de senos y cosenos. El análisis de Fourier es el estudio de la forma general en que las funciones pueden ser representados o aproximadas por sumas de funciones trigonométricas simples. Fourier demostró que representar una función como una suma de funciones trigonométricas, simplifica enormemente el estudio de la transferencia de calor.

 En las ciencias y la ingeniería, el proceso de descomposición de una función en componentes oscilatorios a menudo se denomina análisis de Fourier. Por ejemplo si determinamos qué frecuencias de componentes están presentes en una nota musical, implicaría calcular la transformada de Fourier de una nota musical muestreada. Luego se podría volver a sintetizar el mismo sonido al incluir los componentes de frecuencia. 

#### 2.1.1.1 La transformada de Fourier
Denominada así por Joseph Fourier, es una transformación matemática empleada para transformar señales entre el dominio del tiempo (o espacial) y el dominio de la frecuencia, que tiene muchas aplicaciones en la física y la ingeniería. Es reversible, siendo capaz de transformarse en cualquiera de los dominios al otro. El propio término se refiere tanto a la operación de transformación como a la función que produce. En matemáticas, el análisis armónico o análisis de Fourier estudia la representación de funciones o señales como superposición de ondas "básicas" o armónicos.

## 2.2 Medios de Transmisión Guiado
El propósito de la capa física es transportar un flujo de datos puro de un medio (máquina) a otro. Cada uno tiene su propio segmento en términos de ancho de banda, retardo, costo y facilidad de instalación y mantenimiento. Entre los medios hay diferentes tipos y se clasifican de manera general en medios guiados como: cable de cobre y fibra óptica, y medios no guiados, como radio y láser a través del aire. 

### 2.2.1 Medios Magnéticos
Una de las formas más comunes para transportar datos de una computadora a otra es almacenarlos en cintas magnéticas o medios extraíbles, transportar físicamente la cinta o los discos a la máquina de destino y leer dichos datos ahí. Aunque este método no es tan avanzado como utilizar un satélite de comunicaciones, con frecuencia es más rentable para aplicaciones en las que un ancho de banda alto o el costo por bit transportado es un factor clave. Si hubiera el caso en el que respaldar muchos gigabytes de datos en una segunda máquina, es probable que ninguna otra tecnología de transmisión pueda siquiera acercarse en rendimiento a la cinta magnética. Es cierto que la rapidez de las redes se está incrementando pero también las densidades de las cintas.


## 2.3. Transmisión Inalámbrica
Este medio ha surgido por la necesidad de las personas de estar todo el tiempo conectados en línea a la red sin necesidad de un cable. Para estos usuarios móviles, el cable de par trenzado, el cable coaxial y la fibra óptica no son útiles. Necesitan obtener datos para sus computadoras laptop, celulares, relojes inteligentes, sin estar limitados a la infraestructura de comunicaciones terrestre. La comunicación inalámbrica es la respuesta. Se cree que en el futuro sólo habrá dos clases de comunicación: fibra óptica e inalámbrica. Todos los aparatos fijos (es decir, no móviles): computadoras, teléfonos, faxes, se conectarán con fibra óptica. Y todos los aparatos móviles usarán comunicación inalámbrica. 
### 2.3.1 El espectro electromagnético
Es la distribución energética del conjunto de las ondas electromagnéticas. Referido a un objeto se denomina espectro electromagnético que es cuando emite o absorbe una sustancia. Dicha radiación sirve para identificar la sustancia de manera análoga a una huella dactilar. Los espectros se pueden observar mediante espectroscopios que, además de permitir ver el espectro, permiten realizar medidas sobre el mismo, como son la longitud de onda, la frecuencia y la intensidad de la radiación.

El espectro electromagnético se divide en varios tipos, por ejemplo radiofrecuencia, microondas, infrarrojo, espectro visible, ultravioleta rayos X, rayos gamma. El espectro electromagnético se extiende desde la radiación de menor longitud de onda, como los rayos gamma y los rayos X, pasando por la radiación ultravioleta, la luz visible y la radiación infrarroja, hasta las ondas electromagnéticas de mayor longitud de onda, como son las ondas de radio. 

El comportamiento de las radiaciones electromagnéticas depende de su longitud de onda. Cuando la radiación electromagnética interactúa con átomos y moléculas muy puntuales, su comportamiento también depende de la cantidad de energía por quantum que lleve. Al igual que las ondas de sonido, la radiación electromagnética puede dividirse en octavas.


## 2.4 Diagrama del programa


![](https://github.com/Francmata/-202201-IC7602---Francisco-Mata-Andres-Ramirez-David-Uma-a/blob/main/diagram.jpg)


## 2.5 Ambiente de desarrollo
Este propyecto se desarrollo en el lenguaje de programación Python 3.10 y en 3 computadoras con las siguientes características:

1. Procesador  Intel(R) Core(TM) i5-9300H CPU @ 2.40 GHz
RAM instalada  16,0 GB (15,9 GB utilizable)
Sistema operativo de 64 bits, procesador x64

1. Procesador AMD Ryzen 3 3250U with Radeon Graphics            2.60 GHz 
RAM instalada 12.0 GB (9.94 GB utilizable)  
Tipo de sistema Sistema operativo de 64 bits, procesador x64 

3. Procesador	AMD Ryzen 5 3600 6-Core Processor                 3.59 GHz
RAM instalada	16,0 GB
Tipo de sistema	Sistema operativo de 64 bits, procesador basado en x64


# 3. Conclusiones
Gracias a esta tarea se pudo poner en práctica la creación de un analizador de espectros simple para audios por medio del lenguaje de programación Python. La tarea permite profundizar los conceptos de señales y ondas mediante el uso de módulos de software que implementan la transformada de Fourier, y así transformar por medio de una grafica, las señales entre el dominio del tiempo y el dominio de la frecuencia, lo cual permite evidenciar y entender su comportamiento. Así mismo extraer armónicos específicos para generar tonos de audio para poder analizarlos.


# 4. Referencias
1. Analizador de Espectro. (s.f). ¿Que es un analizador de espectro?. Final Test. Recuperado de: <https://www.finaltest.com.mx/product-p/art-03.htm#:~:text=Un%20analizador%20de%20espectro%20es,ondas%20el%C3%A9ctricas%2C%20ac%C3%BAsticas%20u%20%C3%B3pticas.>

2. Martínez M. (15 mayo 2021). ¿Qué es la transformada de Fourier y para qué sirve?. Recuperado de: <https://www.nobbot.com/educacion/que-es-la-transformada-de-fourier-y-para-que-sirve/>



</font>  
