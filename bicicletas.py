from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funcionTres import calcular_promedio_notas
from funcionCuatro import evaluar_bicicleta



#Paso 1 creo el equipo: 
equipoUno=crear_lista_estudiantes(4)

#paso 2 evaluar las componentes EF, ES, P de la bicicleta
notasEficiencia=crear_lista_notas(50)
notasEstabilidad=crear_lista_notas(50)
notasParecido=crear_lista_notas(50)

#paso 3 calcular la nota promedio de cada componente

eficiencia=calcular_promedio_notas(notasEficiencia)
estabilidad=calcular_promedio_notas(notasEstabilidad)
parecido=calcular_promedio_notas(notasParecido)

#paso 4 evaluo la bicicleta
evalucionFinal=evaluar_bicicleta(eficiencia,estabilidad, parecido)

#paso 5 muestro el resultado

print(f"el resultado del equipo 1 fue: {evalucionFinal}")