import threading
import time
from generador_array import array_potenciado

X = 10000000
resultado = []

hilos = []
start_time = time.time()
for i in range(1):
    h = int(X)
    t = threading.Thread(target=array_potenciado, args=(h,resultado))    
    hilos.append(t)
    t.start()
for x in hilos:
    x.join()
print("All other threads are finished")

#time.sleep(6)
#print(len(resultado))
print("Finalizado en %s seconds ---" % (time.time() - start_time))