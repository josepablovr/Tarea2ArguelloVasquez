from generador_array import generar_array
from generador_array import distribuir_hilos
from generador_array import single_thread
from generador_array import multi_thread
import copy
import time 

resultado = generar_array(10)
resultado1 = copy.copy(resultado)
resultado2 = copy.copy(resultado)

print("1 Hilo:")

start_time = time.time()
single_thread(resultado2)
print("Finalizado en %s seconds ---" % (time.time() - start_time))


print("4 Hilos:")
distribucion = distribuir_hilos(resultado1)

start_time = time.time()
multi_thread(resultado1, distribucion)
print("Finalizado en %s seconds ---" % (time.time() - start_time))

if resultado1 == resultado2:
    print("Exito")
