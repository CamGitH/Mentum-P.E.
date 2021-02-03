# P1.      muestra en pantalla los números primos menores o iguales a 100.
# el numero es dos ya que por deficicion el numero 1 no entra en la cuenta
num = 2
while num <= 100:
    #se define una variable "primo" como verdadera para comprobar si es primo o no
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
    #si la variable "primo" sigue siendo verdadera entonces el numero si es primo
    if primo:
        print(num)

    num = num + 1
#--------------------------------------------------------------------------------------


#P2.       imprima los primeros 100 números primos
# el numero es dos ya que por deficicion el numero 1 no entra en la cuenta
# se tiene la nueva variable contador que llegar[a hasta los 100 primos
num = 2
cont = 0
while cont < 100:
    primo = True
    for i in range(2, num):
        if (num % i == 0):
            primo = False
#si el numero ha probado ser primo al contador se le suma 1
    if primo:
        cont = cont + 1
        print(cont, ". ", num)

    num = num + 1

#--------------------------------------------------------------------------------------
#P3.       informe si el número es par, impar o primo. o
#se le pide al usuario ingresar el numero
n = int(input("Numero del que quiere el informe: "))
#si el mudulo del numero en 2 es 0 entonces el numero es par de lo contrario no es par
if n%2==0:
    print("el numero", n, "es par")
else:
    print("el numero", n, "no es par")
#Prueba para saber si el numero es primo (en caso de no serlo no sedevuelve nada).
primo = True
for i in range(2, n):
    if (n % i == 0):
        primo = False
if primo:
     print("el numero", n, "es primo")


#--------------------------------------------------------------------------------------