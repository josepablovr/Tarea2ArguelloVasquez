import random  # Se importa la libreria de numeros aleatorios
import time  # Se importa la libreria para medir el tiempo
import argparse  # se importa la libreria para pasar argumentos por el shell
import threading  # se importa la libreria para manejar hilos


# Descripción: función encargada de generar el array inicial de X elementos
# Entradas: X = el número de elementos deseado
# Salidas: el array generado
def generar_array(X):
    resultado = []
    n = 0  # se definen las variables iniciales

    for i in range(X):  # ciclo for que se repite X veces
        n = random.randint(0, 100000)  # se genera un número aleatorio
        resultado.append(n)  # se agrega el número generado al array

    return resultado  # retorna el array resultante


# Descripcion: genera los indices para distribuir un array en 4 partes
# Entradas: la longitud (número de elementos) del array
# Salidas: una lista de tuplas con los indices de cada parte
def distribuir_hilos(length):
    num_elem = length // 4  # tamaño mínimo de cada grupo
    sobrantes = length % 4  # residuo de división entre 4
    inicio = 0
    distribucion = []  # se definen las variables iniciales

    for i in range(4):  # ciclo para generar el array de indices
        if sobrantes > 0:  # condición que define el tamaño de cada grupo
            final = inicio + num_elem + 1
            sobrantes -= 1
        else:
            final = inicio + num_elem

        distribucion.append((inicio, final))  # se agregan los nuevos indices
        inicio = final

    return distribucion  # se retorna el array de tuplas con los índices


# Descripcion: funcion que calcula la potencia de los elementos de un array
# Entradas: un array de números
# Salidas: el array modificado con cada elemento al cuadrado
def calc_potencias(resultado):
    for e in resultado:  # se recorre el array
        e = e**2  # se calcula la potencia de cada elemento
        time.sleep(0.000001)  # se agrega un pequeño delay

    return resultado  # se retorna el array modificado


# Descripcion: genera un solo hilo para calcular las potencias del array
# Entradas: el array sobre el que se desea realizar la operación
# Salidas: el array modificado luego de realizar la operación
def single_thread(resultado):
    # se define el hilo
    t = threading.Thread(target=calc_potencias, args=(resultado, ))
    t.start()  # inicia el hilo
    t.join()  # espera a que termine el hilo

    return resultado  # retorna el array resultante


# Descripcion: genera cuatro hilos para calcular las potencias del array
# Entradas: el array sobre el que se desea realizar la operación
# Salidas: el array modificado luego de realizar la operación
def multi_thread(resultado, distribucion):
    resultado_split = []  # lista para almacenar el array subdividido

    for e in range(4):  # ciclo para dividir el array de entrada en 4 subarrays
        dir = distribucion[e]
        resultado_split.append(resultado[dir[0]:dir[1]])
        # se agrega cada sub array dentro de resultado_split

    hilos = []  # lista de hilos

    for i in range(4):  # ciclo para inicializar los 4 hilos
        t = threading.Thread(target=calc_potencias, args=(resultado_split[i],))
        hilos.append(t)  # agrega cada hilo a la lista
        t.start()  # inicia los hilos

    for t in hilos:
        t.join()  # espera a que termine cada hilo

    resultado = []  # reinicia el array de entrada

    for x in range(4):  # ciclo para regenerar el array de entrada modificado
        resultado.append(resultado_split[x])

    return resultado  # retorna el array de entrada modificado


# Descripcion: mide los tiempos de ejecución e imprime los resultados
# Entradas: X = el número de elementos del array, disp = formato de impresión
# Salidas: el array con cada elemento al cuadrado
def medir_tiempo(X, disp):
    t1 = 0
    t4 = 0  # variables para guardar los tiempos de ejecución
    array_inicial = generar_array(X)  # se genera el array inicial
    resultado1 = array_inicial.copy()
    resultado2 = array_inicial.copy()
    # se hacen dos copias del array inicial para realizar los cálculos

    # Procedimiento mediante 1 Hilo
    start_time = time.time()  # se guarda el tiempo de inicio
    single_thread(resultado2)  # llamado a la función para 1 hilo
    t1 = time.time() - start_time  # se calcula el tiempo de ejecución

    # Procedimiento mediante 4 Hilos
    distribucion = distribuir_hilos(X)
    start_time = time.time()  # se guarda el tiempo de inicio
    multi_thread(resultado1, distribucion)  # llamado a la función para 4 hilos
    t4 = time.time() - start_time  # se calcula el tiempo de ejecución

    if disp != 1:  # impresión de resultados en consola
        print("RESULTADOS DEL BENCHMARK:")
        print("--------------------------------------")
        print("1 Hilo:")
        print("Finalizado en %s segundos ---" % t1)
        print("--------------------------------------")
        print("4 Hilos:")
        print("Finalizado en %s segundos ---" % t4)
        print("--------------------------------------")
    else:  # impresión de resultados en un archivo de texto
        f = open("Resultados_Benchmark.txt", "w")
        f.write("RESULTADOS DEL BENCHMARK:")
        f.write("\n --------------------------------------")
        f.write("\n 1 Hilo:")
        f.write("\n Finalizado en %s segundos ---" % t1)
        f.write("\n --------------------------------------")
        f.write("\n 4 Hilos:")
        f.write("\n Finalizado en %s segundos ---" % t4)
        f.close()

    if resultado1 == resultado2:  # verifica el resultado de ambos métodos
        print("Benchmark finalizado exitosamente")
        return resultado1  # se retorna el array resultante


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    # se inicializa el parser
    parser = argparse.ArgumentParser(description='Benchmark')

    # se definen los argumentos necesarios
    parser.add_argument('X', type=int, help="Número de elementos del array")
    parser.add_argument('--file', '-f', nargs='?', const=1, default=0,
                        help="Imprime los resultados en un txt")

    args = parser.parse_args()
    # variable que almacena los argumentos ingresados

    medir_tiempo(args.X, args.file)
    # llamado a la funcion que ejecuta el benchmark
