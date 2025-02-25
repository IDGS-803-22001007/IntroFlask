from flask import Flask, render_template, request
import forms
from flask import g
from flask import flash
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)#objeto de la aplicacion creando la aplicacion

@app.route('/')#decorador o ruta de la aplicacion
def index():
    print('Index2')
    print('Hola{}'.format('g.Nombre'))
    grupo='IDGS703'
    lista=['Brayan','Jorge','Luis']
    return render_template('index.html',grupo=grupo,lista=lista)



@app.before_request
def before_request():
    g.Nombre = 'Brayan'
    print('Antes de la peticion')
    
@app.after_request
def after_request(response):
    print('Despues de la peticion')
    return response



app=Flask(__name__)
app.secret_key='La clave secreta'
csrf = CSRFProtect(app)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    matricula = ""
    edad = ""
    nombre = ""
    apellidos = ""
    email = ""
    alumnos_clase = forms.userForm(request.form)
    if request.method == 'POST' and alumnos_clase.validate():
        matricula = alumnos_clase.matricula.data
        edad = alumnos_clase.edad.data
        nombre = alumnos_clase.nombre.data
        apellidos = alumnos_clase.apellidos.data
        email = alumnos_clase.email.data
        mensaje = "Bienvenido {}".format(nombre)
        flash(mensaje)
    return render_template('alumnos.html', form=alumnos_clase, matricula=matricula, edad=edad, nombre=nombre, apellidos=apellidos, email=email)

@app.route('/cine', methods=['GET', 'POST'])
def cine():
    pagar = ""  

    if request.method == 'POST':
        try:
            nombre = request.form['name']
            cantidad_compradores = int(request.form['compradores'])  
            cineco = int(request.form['cineco'])
            boletos = int(request.form['boletos'])  
            
            boletos_permitidos = (cantidad_compradores + 1) * 7  

            if boletos > boletos_permitidos:
                pagar = f"No puedes comprar más de {boletos_permitidos} boletos (7 por persona)."
            else:
                precio_boleto = 12.00
                total_sin_descuento = boletos * precio_boleto

                if boletos > 5:
                    descuento = 0.15
                elif 3 <= boletos <= 5:
                    descuento = 0.10
                else:
                    descuento = 0.0

                total_con_descuento = total_sin_descuento * (1 - descuento)

                if cineco == 1:
                    total_con_descuento *= 0.9  

                pagar = f"${total_con_descuento:,.2f}"  
        except ValueError:
            pagar = "Error en los datos ingresados, por favor verifica los campos."

    return render_template('cine.html', pagar=pagar)





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
    csrf.init_app(app)
    app.run(debug=True,port=8080)#el debug es para que se actualice automaticamente
    