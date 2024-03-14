from functools import reduce

records = [{"nombre":"panamamericano","area":200,"especies_a":[
            {"nombre_esp":"iguana","num_ej":200}, 
            {"nombre_esp":"garzas","num_ej":250}
            ],"estado_conserv":"malo"},
           {"nombre":"lago de la babilla","area":200,"especies_a":[
            {"nombre_esp":"babilla","num_ej": 8}, 
            {"nombre_esp":"garzas","num_ej": 100}
            ], "estado_conserv":"malo"}]

#calcular usando map, reduce, filter:
#(1) área total de humedales
#(2) filtrar humedales con un total de ejemplares animales > 150
#(3) promedio de número de ejemplares de los humedales

###########################################################

#(1)

area_total = list(map(lambda rec: rec["area"],records))
print(sum(area_total))

#(2)

humedales_ej = list(filter(lambda x: sum(map(lambda y: y["num_ej"], x["especies_a"])) > 150, records))
print(humedales_ej)

#(3)
map_especies = list(map(lambda r: r["especies_a"],records))
lista_especies = reduce(lambda x,y:x+y,map_especies)
lista_num_ej = list(map(lambda x: x["num_ej"],lista_especies))
promedio = reduce(lambda x,y: x+y,lista_num_ej)/len(lista_num_ej)
print(promedio)