import random  # Se importa la libreria de numeros aleatorios
import threading
import time


def generar_array(X):
    resultado = []
    n = 0
    for n in range(X):
        n = n = random.randint(0, 10)
        n = pow(n, 2)
        resultado.append(n)

    return resultado


def mensaje(X):
    print("flag")


def distribuir_hilos(resultado, n_hilos):
    tamaño = len(resultado)
    distribucion = []
    final = tamaño - 1
    for i in range(n_hilos):
        inicio = final - tamaño//n_hilos + 1
        distribucion.append((inicio, final))
        final = inicio - 1
        tamaño = final + 1
        n_hilos -= 1

    distribucion.reverse()
    return distribucion


def potencias(resultado, direccion):
    for e in range(direccion[0], direccion[1]+1):
        resultado[e] = pow(resultado[e], 2)
    return resultado


def single_thread(resultado):
    start_time = time.time()
    final = len(resultado)-1
    direccion = (0, final)
    t = threading.Thread(target=potencias, args=(resultado, direccion))
    t.start()
    t.join()
    print("Finalizado en %s seconds ---" % (time.time() - start_time))
    return resultado


def multi_thread(resultado, distribucion, n_hilos):
    start_time = time.time()
    hilos = []

    for i in range(n_hilos):
        dir = distribucion[i]
        t = threading.Thread(target=potencias, args=(resultado, dir))
        hilos.append(t)
        t.start()
    for x in hilos:
        x.join()
    print("Finalizado en %s seconds ---" % (time.time() - start_time))
    return resultado
