import numpy as np   
import pyaudio   
import struct    
import matplotlib.pyplot as plt   
import wave   
import keyboard   
import pickle  
  
  
def reproductor(archivo):  
     
     
    sample_format = pyaudio.paInt16  #Es el mas comun para expresar el audio  
    channels = 1 #Depende de la cantidad de entradas que use, en nuestro caso solo es 1  
    fs = 20000  #Cantidad de frames 
 
    file = open(archivo, 'rb') #Se carga el archivo atm  
    obj_1 = pickle.load(file) #carga los numeros enteros del gráfico  
    obj_2 = pickle.load(file)  #carga los frames  
    chunk = 1024    #Tamanno de chunks      
     
    pa = pyaudio.PyAudio()   #Interfaz de pyaudio  
    stream = pa.open(format = sample_format,channels = channels,rate = fs,output = True)   #Se abre el stream con la configuracion almacenada en el archivo wave  
  
 
  
    #Se imprime el menu del reproductor  
    print("--------------------------------------------------------------")  
    print("Instrucciones")  
    print("Con la tecla Escape se sale de la aplicacion.")  
    print("Con la tecla Espacio pausa la aplicacion.")  
    print("Con la tecla Enter reanuda la reproduccion.")  
    print("Para salir de la aplicacion con Escape, la aplicacion debe estar reproduciendose.\n")  
    print("--------------------------------------------------------------")  
  
    print("Usted accedio al Reproductor, aprete 'enter' para empezar a reproducir.")  
  
    #Espera para empezar a reproducir   
    keyboard.wait('enter')  
  
      
  
    # Se crea el grafico  
    # Me devuelve una lista dentro de un intervalo  
    fig, (ax1, ax2) = plt.subplots(2) #se crea las graficas  
    x_frecuencia = np.arange(0, 2 * chunk, 2)  # [0,2,4,6,....,2048]  
    x_furier = np.linspace(0, fs, chunk)  # [0,1024,2048,....,RATE]  
  
    # Coloco titulo a cada uno   
    ax1.set_title('Frecuencia')  
    ax2.set_title('Furier')  
  
    # Establezco los limites de cada grafico  
    ax1.set_xlim(0, chunk)  
    ax1.set_ylim(-fs, fs)  
  
    ax2.set_xlim(20, fs)  
    # La salida de los calculos de furier varian de 0 a 1, meto -1 para verla mejor  
    ax2.set_ylim(0, 1)  
  
    line_frecuencia, = ax1.plot(x_frecuencia, np.random.rand(chunk), 'r')  
    # La representacion de frecuencia siempre se hace en graficos semilogaritmicos  
    line_furier, = ax2.semilogx(x_furier, np.random.rand(chunk), 'b')  
  
    fig.show()  
    cont = 0  
  
  
  
  
    #Se reproduce el audio y se muestran los graficos     
    for x in obj_1:     
        stream.write(obj_2[cont])  #Se reproducen los datos guardados  
  
        #Se muestra la grafica con los datos guardados  
        line_frecuencia.set_ydata(x)    
        line_furier.set_ydata(np.abs(np.fft.fft(x))*2/(11000*chunk))   
        fig.canvas.draw()   
        fig.canvas.flush_events()  
        #Condiciones de pausar el analizador y reanudar  
        if(keyboard.is_pressed('space')):  
            while 1:  
                line_frecuencia.set_ydata(x)   # Actualiza el grafico  
                line_furier.set_ydata(np.abs(np.fft.fft(x)) * 2 / (11000 * chunk))  
                fig.canvas.draw()  
                fig.canvas.flush_events()  
                if(keyboard.is_pressed('enter')):  
                    break
        
        if(keyboard.is_pressed('escape')):  
            plt.close('all')
            break

        cont=cont+1   
  
          
    stream.stop_stream()   #Detener stream  
    stream.close()    #Finalizar stream  
    pa.terminate() #Terminar la interfaz  
    plt.close('all') 
  
  
  
  
#Funcion del analizador para grabar  
def analizadorGrabar(archivo):   
    chunk = 1024  #Tamanno de chunks  
    sample_format = pyaudio.paInt16  #Es el mas comun para expresar el audio  
    channels = 1 #Depende de la cantidad de entradas que use, en nuestro caso solo es 1  
    fs = 20000  #Cantidad de frames  
    p = pyaudio.PyAudio()  #Se llama a pyaudio, es la libreria de audio utilizada  
    file = open(archivo[:-4]+'.atm','wb') #Se abre el archivo atm para guardar los archivos  
  
  
    stream = p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)  # Se abre el stream  
  
  
    # Datos que se guardan en el archivo atm  
    frames = []  #Lista con los frames en formato paInt16  
    numbers=[] #Lista de enteros para graficar  
  
  
    #Se imprime el menu del analizador  
    print("--------------------------------------------------------------")  
    print("Instrucciones")  
    print("Con la tecla Escape se sale de la aplicacion.")  
    print("Con la tecla Espacio pausa la aplicacion.")  
    print("Con la tecla Enter reanuda la grabacion.")  
    print("Para salir de la aplicacion con Escape, la aplicacion debe estar grabando.\n")  
    print("--------------------------------------------------------------")  
  
    print("Usted accedio al Analizador, aprete 'enter' para empezar a grabar.")  
  
    #Espera para empezar a grabar   
    keyboard.wait('enter')  
  
  
  
    fig, (ax1, ax2) = plt.subplots(2) #se crea las graficas  

    # Me devuelve una lista dentro de un intervalo  
    x_frecuencia = np.arange(0, 2 * chunk, 2)  # [0,2,4,6,....,2048]  
    x_furier = np.linspace(0, fs, chunk)  # [0,1024,2048,....,RATE]  
  
    # Coloco titulo a cada uno  
    ax1.set_title('Frecuencia')  
    ax2.set_title('Furier')  
  
    # Establezco los limites de cada grafico  
    ax1.set_xlim(0, chunk)  
    ax1.set_ylim(-30000, 30000)  
  
    ax2.set_xlim(20, fs)  
    # La salida de los calculos de furier varian de 0 a 1, meto -1 para verla mejor  
    ax2.set_ylim(-1, 1)  
  
    line_frecuencia, = ax1.plot(x_frecuencia, np.random.rand(chunk), 'r')  
    # La representacion de frecuencia siempre se hace en graficos semilogaritmicos  
    line_furier, = ax2.semilogx(x_furier, np.random.rand(chunk), 'b')  
  
    fig.show()  

    
    # Grabar el audio y guardarlo en la lista de frames  
    print('Grabando')  
    while(not keyboard.is_pressed('escape')): #Graba hasta que se presione la tecla escape  
        data = stream.read(chunk) #Lee el microfono  
        frames.append(data) #Guarda los frames  
        dataInt = struct.unpack(str(chunk) + 'h', data)  # Es para pasar a formato entero para graficar  
        numbers.append(dataInt) #Guarda los datos en entero para graficar  
  
        # Actualiza el grafico  
        line_frecuencia.set_ydata(dataInt)     
        line_furier.set_ydata(np.abs(np.fft.fft(dataInt)) * 2 / (11000 * chunk))   
        fig.canvas.draw()  
        fig.canvas.flush_events()  
  
        #Condiciones de pausar el analizador y reanudar  
        if(keyboard.is_pressed('space')):  
            while 1:  
                line_frecuencia.set_ydata(dataInt)   # Actualiza el grafico  
                line_furier.set_ydata(np.abs(np.fft.fft(dataInt)) * 2 / (11000 * chunk))  
                fig.canvas.draw()  
                fig.canvas.flush_events()  
                if(keyboard.is_pressed('enter')):  
                    break  
  
  
  
    #Pausar el stream y cerrarlo 
    plt.close('all')  
    stream.stop_stream()  
    stream.close()  
    #Terminar la interfaz de pyaudio  
    p.terminate()  
    print('Finalizo la Grabacion')  
    
  
    #Guardar el audio en un archivo wave  
    wf = wave.open(archivo, 'wb')  
    wf.setnchannels(channels)  
    wf.setsampwidth(p.get_sample_size(sample_format))  
    wf.setframerate(fs)  
    wf.writeframes(b''.join(frames))  
    wf.close()  
  
    #Guardo los datos en el archivo .atm  
    pickle.dump(numbers, file)  
    pickle.dump(frames, file)  
    file.close()  
  
  
def analizadorwave(archivo):  
    file = open(archivo[:-4]+'.atm', 'wb')  
    chunk = 1024    #Tamanno de chunks      
    af = wave.open(archivo, 'rb')    #Abrir el archivo de audio  
    pa = pyaudio.PyAudio()   #Interfaz de pyaudio  
    stream = pa.open(format = pa.get_format_from_width(af.getsampwidth()),     
                    channels = af.getnchannels(),     
                    rate = af.getframerate(),     
                    output = True)   #Se abre el stream con la configuracion almacenada en el archivo wave  
      
    # Se crea el grafico  
    # Me devuelve una lista dentro de un intervalo  
    fig, (ax1, ax2) = plt.subplots(2) #se crea las graficas  
    x_frecuencia = np.arange(0, 2 * chunk, 2)  # [0,2,4,6,....,2048]  
    x_furier = np.linspace(0, af.getframerate(), chunk)  # [0,1024,2048,....,RATE]  
  
    # Coloco titulo a cada uno   
    ax1.set_title('Frecuencia')  
    ax2.set_title('Furier')  
  
    # Establezco los limites de cada grafico  
    ax1.set_xlim(0, chunk)  
    ax1.set_ylim(-30000, 30000)  
  
    ax2.set_xlim(20, af.getframerate())  
    # La salida de los calculos de furier varian de 0 a 1, meto -1 para verla mejor  
    ax2.set_ylim(0, 1)  
  
    line_frecuencia, = ax1.plot(x_frecuencia, np.random.rand(chunk), 'r')  
    # La representacion de frecuencia siempre se hace en graficos semilogaritmicos  
    line_furier, = ax2.semilogx(x_furier, np.random.rand(chunk), 'b')  
    frames=[]  
    numbers=[]  
    fig.show()  
    data = af.readframes(chunk)  
  
    while data != '' or data!= b'':  
        try:  
            stream.write(data)  
            data = af.readframes(chunk)  
            frames.append(data) #Guarda los frames  
  
            dataInt = struct.unpack(str(chunk) + 'h', data)  # Es para pasar a formato entero para graficar  
            numbers.append(dataInt) #Guarda los datos en entero para graficar  
  
            # Actualiza el grafico  
            line_frecuencia.set_ydata(dataInt)     
            line_furier.set_ydata(np.abs(np.fft.fft(dataInt)) * 2 / (11000 * chunk))   
            fig.canvas.draw()  
            fig.canvas.flush_events()  
        except:  
            break  
  
  
          
    stream.stop_stream()   #Detener stream  
    stream.close()    #Finalizar stream  
    pa.terminate() #Terminar la interfaz  
    plt.close('all') 
     
    #Guardo los datos en el archivo .atm  
    pickle.dump(numbers, file)  
    pickle.dump(frames, file)  
    file.close()  
 
  
  
  
def main():  
  
    while 1:  
        print("--------------------------------------------------------------")  
        print("MENU DE LA APLICACION AUTRUM\n")  
        print("Al escribir '0' se cierra la aplicacion.")  
        print("Al escribir '1' se accede al Analizador.")  
        print("Al escribir '2' se accede al Reproductor.") 
        print("Al escribir '3' se accede al Analizador por archivo.")  
        print("Al escribir 'M' se muestran las opciones de nuevo.")  
        print("--------------------------------------------------------------")  
        argument = input()  
        match argument:  
            case '0':  
                return True  
            case '1':  
                print("Ha escogido el Analizador. Escriba el nombre del archivo con extension .wav: ")  
                x = input()  
                analizadorGrabar(x)  
            case '2':  
                print("Ha escogido el Reproductor. Escriba el nombre del archivo con extension .atm: ")  
                y = input()  
                reproductor(y)  
            case '4':   
                print("--------------------------------------------------------------")  
                print("MENU DE LA APLICACION AUTRUM\n")  
                print("Al escribir '1' se accede al Analizador.")  
                print("Al escribir '2' se accede al Reproductor.") 
                print("Al escribir '3' se accede al Analizador por archivo.")   
                print("Al escribir 'M' se muestran las opciones de nuevo.")  
                print("--------------------------------------------------------------")  
            case '3': 
                print("Ha escogido el Analizador. Escriba el nombre del archivo con extension .wav: ") 
                x = input()  
                analizadorwave(x) 
  
  
main()