from flask import Flask

app = Flask(__name__)#objeto de la aplicacion creando la aplicacion

@app.route('/')#decorador o ruta de la aplicacion
def index(): 
    return 'Hola Mundo'


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


@app.route('/default')
@app.route('/default/<string:nom>')
def func(nom='Brayan'): 
    return 'El nombre de nom es: ' + nom



if __name__ == '__main__': #indicamos de donde se ejecuta la aplicacion
    app.run(debug=True,port=8080)#el debug es para que se actualice automaticamente
    