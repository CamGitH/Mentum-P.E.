from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


# --------------------------------------------------------------------------------------
# P1.      muestra en pantalla los números primos menores o iguales a 100.
# el numero NUM es dos ya que por deficicion el numero 1 no entra en la cuenta

@app.route('/1/', methods=['POST'])
def p1():
    ans = ''
    if request.method=='POST':
        num = 2
        while num <= 100:
            # se define una variable "primo" como verdadera para comprobar si es primo o no
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
            # si la variable "primo" sigue siendo verdadera entonces el numero si es primo
            if primo:
                ans= ans, num

            num = num + 1

    return render_template('index.html', ans=ans)


# --------------------------------------------------------------------------------------
# P2.       imprima los primeros 100 números primos
# el numero es dos ya que por deficicion el numero 1 no entra en la cuenta
# se tiene la nueva variable contador que llegar[a hasta los 100 primos
@app.route('/2/', methods=['POST'])
def p2():
    ans = ''
    if request.method=='POST':
        num = 2
        cont = 0
        while cont < 100:
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
            # si el numero ha probado ser primo al contador se le suma 1
            if primo:
                cont = cont + 1
                ans = ans, cont,':', num


            num = num + 1

    return render_template('index.html', ans=ans)


# --------------------------------------------------------------------------------------
# P3.       informe si el número es par, impar o primo. o
# se le pide al usuario ingresar el numero
# si el mudulo del numero en 2 es 0 entonces el numero es par de lo contrario no es par
@app.route('/3/', methods=['POST', 'GET'])
def p3():
    ans = ''
    if request.method=='POST' and 'numero' in request.form:
        n = int(request.form.get('numero'))
        if n % 2 == 0:
            ans = "el numero", n, "es par"
        else:
            ans = "el numero", n, "no es par"
        # Prueba para saber si el numero es primo (en caso de no serlo no sedevuelve nada).
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
        if primo:
            ans = ans, "el numero", n, "es primo"

    return render_template('index.html', ans=ans)




# --------------------------------------------------------------------------------------
