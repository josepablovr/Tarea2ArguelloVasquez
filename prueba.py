from generador_array import generar_array
from generador_array import distribuir_hilos
from generador_array import single_thread
from generador_array import multi_thread


resultado = generar_array(5000000)
# distribucion = distribuir_hilos(resultado, 4)

print("1 Hilo:")
single_thread(resultado)

distribucion = distribuir_hilos(resultado, 2)
print("2 Hilos:")
multi_thread(resultado, distribucion, 2)

distribucion = distribuir_hilos(resultado, 4)
print("4 Hilos:")
multi_thread(resultado, distribucion, 4)

distribucion = distribuir_hilos(resultado, 8)
print("8 Hilos:")
multi_thread(resultado, distribucion, 8)
