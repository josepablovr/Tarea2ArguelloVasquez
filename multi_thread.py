import threading
import time
from generador_array import potencias


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
