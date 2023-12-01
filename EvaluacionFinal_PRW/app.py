from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pagp.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            ingresatunombre = request.form['ingresatunombre']
            ingresatuedad = int(request.form['ingresatuedad'])
            ingresalacantidaddetarrosdepinturaacomprar = int(request.form['ingresalacantidaddetarrosdepinturaacomprar'])

        except ValueError:
            return 'Error en los datos ingresados. Asegúrate de ingresar datos válidos.'

        # Asumimos un precio de 9000 dólares por tarro de pintura
        precio_por_tarro = 9000

        # Calculamos el total a pagar sin descuento
        total_sin_descuento = precio_por_tarro * ingresalacantidaddetarrosdepinturaacomprar

        # Determinamos el descuento aplicable según la edad
        if ingresatuedad < 18:
            descuento = 0
        elif ingresatuedad >= 18 and ingresatuedad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25



            # Calculamos el total a pagar con el descuento aplicado
        total = total_sin_descuento * (1 - descuento)
        descuento_aplicado = total_sin_descuento - total

        # Mostramos el resultado
        mensaje = f"""Cálculo de compras:
        <br>Nombre: {ingresatunombre}
        <br>Total sin descuento: ${total_sin_descuento}
        <br>El descuento es: ${descuento_aplicado}
        <br>El total a pagar es de: ${total}"""

        return render_template('ejercicio1.html', resultado=mensaje)
    return render_template('ejercicio1.html')



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        try:
            ingresatunombre = request.form['ingresatunombre']
            ingresatucontraseña = request.form['ingresatucontraseña']


            usuarios={
                "juan": "admin",
                "pepe": "user"
            }

            if ingresatunombre in usuarios and usuarios[ingresatunombre] == ingresatucontraseña:
                if ingresatunombre == 'juan':
                    mensaje = f"Bienvenido Administrador {ingresatunombre}"
                else:
                    mensaje = f"Binevenido usuario {ingresatunombre}"
            else:
                mensaje ='Usuario o constraseña incorrecta'

        except ValueError:
            mensaje = 'Error en los datos ingresados. Asegúrate de ingresar datos válidos.'

    return render_template('ejercicio2.html', resultado=mensaje)


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run(port=5001)
