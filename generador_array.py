import random  # Se importa la libreria de numeros aleatorios
import threading
import time


def generar_array(X):
    resultado = []
    n = 0
    for n in range(X):
        n = n = random.randint(0, 1000)
        n = pow(n, 2)
        resultado.append(n)

    return resultado


def mensaje(X):
    print("flag")


def distribuir_hilos(resultado):
    tamaño = len(resultado)
    distribucion = []
    final = tamaño - 1
    n_hilos = 4
    for i in range(n_hilos):
        inicio = final - tamaño//n_hilos + 1
        distribucion.append((inicio, final + 1))
        final = inicio - 1
        tamaño = final + 1
        n_hilos -= 1

    distribucion.reverse()
    return distribucion


def potencias(resultado, direccion):
    for e in range(direccion[0], direccion[1]):
        resultado[e] = resultado[e]**2
        for e in range(2):
            time.sleep(0.3)
            

    return resultado


def single_thread(resultado):
    start_time = time.time()
    final = len(resultado)
    direccion = (0, final)
    t = threading.Thread(target=potencias, args=(resultado, direccion))
    t.start()
    t.join()
    print("Finalizado en %s seconds ---" % (time.time() - start_time))
    return resultado


def multi_thread(resultado, distribucion):
    start_time = time.time()
    hilos = []

    for i in range(4):
        dir = distribucion[i]
        t = threading.Thread(target=potencias, args=(resultado, dir))
        t.start()
        hilos.append(t)        
    for t in hilos:
        t.join()
    print("Finalizado en %s seconds ---" % (time.time() - start_time))
    return resultado
