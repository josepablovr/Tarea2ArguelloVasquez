import threading
import time
from generador_array import potencias


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
