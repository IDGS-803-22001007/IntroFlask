from flask import Flask, render_template, request



app = Flask(__name__)#objeto de la aplicacion creando la aplicacion

@app.route('/')#decorador o ruta de la aplicacion
def index():
    grupo='IDGS703'
    lista=['Brayan','Jorge','Luis']
    return render_template('index.html',grupo=grupo,lista=lista)


@app.route('/OperasBas')#decorador o ruta de la aplicacion
def Operas():
    return render_template('OperasBas.html')

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':
        num1 = request.form.get('n1')
        num2 = request.form.get('n2')
        resultado = int(num1) + int(num2)
        return render_template('OperasBas.html', resultado=resultado)


@app.route('/ejemplo1')#decorador o ruta de la aplicacion
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')#decorador o ruta de la aplicacion
def ejemplo2():
    return render_template('ejemplo2.html')






@app.route('/hola')#decorador o ruta de la aplicacion
def hola(): 
    return 'hola!!!!!'


@app.route('/user/<string:user>')#decorador o ruta de la aplicacion  
def user(user): 
    return f'Hola {user}!!!'



@app.route('/suma/<int:n>')#decorador o ruta de la aplicacion
def numero(n): 
    return 'numero: {}'.format(n)




@app.route('/user/<string:user>/<int:id>')#decorador o ruta de la aplicacion  
def username(user,id): 
    return f'Hola {user} ID:{id}!!!'



@app.route('/suma/<float:n1>/<float:n2>')#decorador o ruta de la aplicacion
def suma(n1,n2): 
    return 'La suma es: {}!!!'.format(n1+n2)


# @app.route('/default')
# @app.route('/default/<string:nom>')
# def func(nom='Brayan'): 
#     return 'El nombre de nom es: ' + nom



@app.route('/form1')
def form1():
    return '''
        <form>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        </br>
    '''





if __name__ == '__main__': #indicamos de donde se ejecuta la aplicacion
    app.run(debug=True,port=8080)#el debug es para que se actualice automaticamente
    