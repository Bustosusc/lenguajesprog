def erastostenes(n):
    primes = []
    isprime = []
    for i in range(0,n,1):
        if i == 0 or i == 1:
            isprime.append(0)
        else:
            isprime.append(i)

    for i in range(2,n,1):
        if isprime[i]:
            primes.append(i)
            h = 2
            while i*h < n:
                isprime[i*h] = 0
                h = h + 1
    return primes, isprime

def numeros (n,x):
    isprime = []
    for i in range(0,n,1):
        if i == 0 or i == 1:
            isprime.append(0)
        else:
            isprime.append(i)
    return isprime

def lazy_erastostenes(n,x,isprime):
    primes = []

    i = 2
    while True:
        if isprime[i]:
            yield i
            h = 2
            while i*h < n:
                isprime[i*h] = 0
                h = h + 1
        i = i + 1
           

n = 20
x = 4
num = numeros(n,x)
gen_prime = lazy_erastostenes(n,x,num)
print("Erastostenes impaciente:",erastostenes(n))
print("")
lista_prime1 = [next(gen_prime) for _ in range(x)]
print(f"primeros {x} primos entre 0 y {n} {lista_prime1}")
lista_prime2 =  [next(gen_prime) for _ in range(x)]
print(f"siguentes {x} primos entre 0 y {n} {lista_prime2}")