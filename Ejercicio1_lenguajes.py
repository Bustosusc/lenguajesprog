def op1(a,b):
    return a+b

def op2(a,b):
    return a*b

def op3(a,b):
    return a**b

def op4(a,b):
    return a-b


#operacion = int(input("que operacion? 1-suma, 2-multiplicacion, 3-potencia, 4-resta "))
val1 = int(input("ingrese valor 1: "))
val2 = int(input("ingrese valor 2: "))


lista_func = [op1, op2, op3, op4]
resultado = map(lambda rec: rec(val1,val2),lista_func)
a = list(resultado)
