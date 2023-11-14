from flask import Flask, render_template
# captuando todo flask 
app = Flask(__name__)
# ruta raiz
@app.route('/')
def inicio():
  titulo = "Bienvenido"
  return render_template('inicio.html', titulo=titulo)


# ruta mi nombre
@app.route('/benjamin')
def nombre():
   return render_template('')


# bloque de prueba para flask 
if __name__ == "__main__":
  app.run(debug=True)