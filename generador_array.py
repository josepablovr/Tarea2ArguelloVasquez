import random  # Se importa la libreria de numeros aleatorios
import time
import copy
import argparse
from multiprocessing import Process


def generar_array(X):
    resultado = list(range(X))
    # n = 0
    # for n in range(X):
    #    n = n = random.randint(0, 100000)
    #    n = pow(n, 2)
    #    resultado.append(n)

    return resultado


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
    # array = []
    for e in range(direccion[0], direccion[1]):
        resultado[e] = resultado[e]**2
        # time.sleep(0.00000001)
        # for e in range(e):
        # array.insert(e, resultado[e])
    return resultado


def single_thread(resultado):

    if __name__ == "__main__":

        dir = (0, len(resultado))
        t = Process(target=potencias, args=(resultado, dir))
        t.start()
        t.join()

    return resultado


def multi_thread(resultado, distribucion):

    hilos = []
    if __name__ == "__main__":
        for i in range(4):
            dir = distribucion[i]
            t = Process(target=potencias, args=(resultado, dir))
            hilos.append(t)
            t.start()

        for t in hilos:
            t.join()

    return resultado


def medir_tiempo(X, disp):
    t1 = 0
    t4 = 0
    resultado = generar_array(X)
    resultado1 = copy.copy(resultado)
    resultado2 = copy.copy(resultado)

    # 1 Hilo
    start_time = time.time()
    single_thread(resultado2)
    t1 = time.time() - start_time

    # 4 Hilos
    distribucion = distribuir_hilos(resultado1)
    start_time = time.time()
    multi_thread(resultado1, distribucion)
    t4 = time.time() - start_time

    if disp != 1:
        print("RESULTADOS DEL BENCHMARK:")
        print("--------------------------------------")
        print("1 Hilo:")
        print("Finalizado en %s segundos ---" % t1)
        print("--------------------------------------")
        print("4 Hilos:")
        print("Finalizado en %s segundos ---" % t4)
        print("--------------------------------------")
    else:
        f = open("Resultados_Benchmark.txt", "w")
        f.write("RESULTADOS DEL BENCHMARK:")
        f.write("\n --------------------------------------")
        f.write("\n 1 Hilo:")
        f.write("\n Finalizado en %s segundos ---" % t1)
        f.write("\n --------------------------------------")
        f.write("\n 4 Hilos:")
        f.write("\n Finalizado en %s segundos ---" % t4)
        f.close()

    if resultado1 == resultado2:
        print("Benchmark finalizado exitosamente")
        return resultado1


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='Benchmark')

    parser = argparse.ArgumentParser()
    parser.add_argument("X", help="Benchmark de un recorrido de array",
                        type=int)
    parser.add_argument("display", nargs="?",
                        type=int)

    args = parser.parse_args()

    medir_tiempo(args.X, args.display)
