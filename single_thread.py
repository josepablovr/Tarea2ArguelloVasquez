import threading
import time

from generador_array import potencias


def single_thread(resultado):
    start_time = time.time()
    final = len(resultado)-1
    direccion = (0, final)
    t = threading.Thread(target=potencias, args=(resultado, direccion))
    t.start()
    t.join()
    print("Finalizado en %s seconds ---" % (time.time() - start_time))
    return resultado
