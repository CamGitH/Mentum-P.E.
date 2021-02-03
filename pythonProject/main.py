# P1.      muestra en pantalla los números primos menores o iguales a 100.

num = 2
while num < 100:
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False

    if primo:
        print(num)

    num = num + 1

#P2.       imprima los primeros 100 números primos

num = 2
cont = 0
while cont < 100:
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False

    if primo:
        cont = cont + 1
        print(cont, ". ", num)

    num = num + 1


#P3.       informe si el número es par, impar o primo. o

n = int(input("Numero del que quiere el informe: "))
if n%2==0:
    print("el numero", n, "es par")
else:
    print("el numero", n, "no es par")

primo = True
for i in range(2, n):
    if (n % i == 0):
        primo = False
if primo:
     print("el numero", n, "es primo")


