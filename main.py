from flask import Flask, redirect, url_for

from controllers.Postulaciones_controller import postulaciones_bp
from controllers.Validaciones_controller import validaciones_bp

# Para ejecutar proyecto, usar en CMD -> flask --app main --debug run
app = Flask(__name__)

app.register_blueprint(postulaciones_bp)
app.register_blueprint(validaciones_bp)

# errorhandler 404
@app.errorhandler(404)
def page_not_found(error):
    # print(error)
    return redirect(url_for('postulaciones.postulaciones'))
# main
if __name__ == '__main__':
    app.run(debug=True)