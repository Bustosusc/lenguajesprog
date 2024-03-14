from functools import reduce

#promedio de cada estudiante con map

#def promedio(a):

#    notas = 0
#    for i in range(0,len(a[1]),1):
#        notas = notas + a[1][i]

#    prom = notas/len(a[1])
#    resultado = print("el promedio del estudiante "+ a[0] + " es: ",prom)
#    print("")
#    return notas,prom

#def edad_mayor(a):

#    N = 22
#    if a[2] > N:
#        resultado = print("el estudiante "+ a[0] + " tiene una edad mayor a: ",N)
#        print("")
#        return resultado

#def promedio_total(a,b):
#    return a[0] + b[0]
    
    
lista_reg = [{"nombre":"Sebastian","edad":24,"notas":[3.0,4.0,5.0]},
            {"nombre":"Valentina","edad":20,"notas":[2.5,3.8,4.3]},
            {"nombre":"Santiago","edad":18,"notas":[5.0,4.7,4.0]},
            {"nombre":"Natalia","edad":25,"notas":[4.6,3.4,4.5]},
            {"nombre":"Kevin","edad":30,"notas":[2.0,3.5,3.9]}]

#buscar como definir una matriz
#lista_notas = []
#lista_nombres = []
#lista_edad = []
#iterable = []
#for i in range(0,len(lista_reg),1):
#    lista_notas.append(0)
#    lista_nombres.append(0)
#    lista_edad.append(0)
#    iterable.append(0)

#for i in range(0,len(lista_reg),1):
#    lista_notas[i] = lista_reg[i][5]
#    lista_nombres[i] = lista_reg[i][1]
#    lista_edad[i] = lista_reg[i][3]
#    iterable[i] = lista_nombres[i],lista_notas[i],lista_edad[i]
    #print(lista_notas)
    #print(lista_nombres)
    #print(iterable)
#lista_map_notas = list(map(promedio,iterable))
#print(lista_map_notas)

#lista_total_notas = []
#for i in range(0,len(lista_map_notas),1):
#    lista_total_notas.append(lista_map_notas[i][0])

#print(lista_total_notas)
#filtrar estudiantes con edad > N con filter

#lista_edad_mayor = list(filter(edad_mayor,iterable))

#promedio general con reduce

#lista_promedio_gen = reduce(lambda x,y: x+y,lista_total_notas)
#print("el promedio general del grupo es:",lista_promedio_gen/(len(lista_notas[0])*len(lista_notas)))


###############################################################################
#correccion

promedios = list(map(lambda record: sum(record["notas"])/len(record["notas"]),lista_reg))
print(promedios)

#filter

edad = 22
lista_filtrada = list(filter(lambda rec: rec["edad"] >= edad,lista_reg))
print(lista_filtrada)

#promedio de estudiantes con reduce

promedio_general = reduce(lambda x,y: x+y,promedios)/len(promedios)
print(promedio_general)