import math
#funcion impaciente(eager)
#def mult(n,m):
#    mults = [n for n in range(n+1) if n % m == 0]
#    return mults

#funcion perezosa
#def mult_lazy(n,m):
#    num = 0
#    while True:
#        if num % m == 0:
#            yield num
#        num += 1

#m = int(input("Ingrese m:"))
#n = int(input("Ingrese el numero de terminos:"))

#mults = mult(n,m)
#gen_mult = mult_lazy(n,m)

#first_100 = [next(gen_mult) for _ in range(100)]
#print(f"primeros 100:{first_100}")
#next_100 = [next(gen_mult) for _ in range(100)]
#print(f"primeros 100:{next_100}")
#print(mults)

#def e(x,n):
#    resultado = 0
#    for i in range(0,n,1):
#        resultado = resultado + (x**i/math.factorial(i))
#    return resultado

#print(e(1,4))

#Lazy evaluation de euler

def lazy_sum(x,n):
    sum = 0.0
    i = 0
    while True:
        sum += x**i/math.factorial(i)
        i += 1
        yield sum

x = int(input("ingrese x "))
n = int(input("ingrese n "))

gen_sum = lazy_sum(x,n)
list_aprox1 = [next(gen_sum) for _ in range(n)]
aprox1 = sum(list_aprox1)
list_aprox2 = [next(gen_sum) for _ in range(n)]
aprox2 = sum(list_aprox2)
print(f"Aproximacion con primeros {n} {aprox1}")
print(f"Aproximacion con siguentes {n} {aprox2}")