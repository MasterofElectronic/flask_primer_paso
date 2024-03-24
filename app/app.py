from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    lista=['python', 'JavaScript', 'PHP', 'Django']
    
    data={
        'titulo': 'Index',
        'bienvenida':'saludo',
        'cursos':lista,
        'numero_cursos':len(lista)
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data={
        'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad

    }
    return render_template('contacto.html')

def query_string():
    print(request)
    return "Ok"

def page_not_found(error):
    return render_template('404.html'), 404
    #return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)

