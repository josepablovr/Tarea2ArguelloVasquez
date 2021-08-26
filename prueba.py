from generador_array import generar_array
from generador_array import distribuir_hilos
from single_thread import single_thread
from multi_thread import multi_thread


resultado = generar_array(5)

resultado1 = resultado
resultado2 = resultado
# distribucion = distribuir_hilos(resultado, 4)


distribucion = distribuir_hilos(resultado1, 4)
print(resultado1)
print("4 Hilos:")
multi_thread(resultado1, distribucion, 4)
print(resultado1)


print(resultado2)
print("1 Hilo:")
single_thread(resultado2)
print(resultado)