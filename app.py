from flask import Flask

app = Flask(__name__)


#http://localhost:5000/
@app.route('/')
def inicio():gi
    return 'Hola mundo...'


# from flask import Flask, render_template, url_for, request
# from flask_migrate import Migrate
# from werkzeug.utils import redirect
#
# from database import db
# from forms import PersonaForm
# from models import Persona
#
# app = Flask(__name__, template_folder='app/base/templates')
# app._static_folder = 'app/base/static'
#
# # Configuración de la bd
# USER_DB = 'postgres'
# PASS_DB = 'admin'
# URL_DB = 'localhost'
# NAME_DB = 'flask_form'
# FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # Inicialización del objeto db de sqlalchemy
# db.init_app(app)
#
# # Configurar flask-migrate
# migrate = Migrate()
# migrate.init_app(app, db)
#
# # Configurar flask-wtf
# app.config['SECRET_KEY'] = 'llave_secreta'
#
#
# @app.route('/')
# @app.route('/index')
# @app.route('/index.html')
# def inicio():
#     # Listado de personsas
#     # personas = Persona.query.all()
#     personas = Persona.query.order_by('id')
#     total_personas = Persona.query.count()
#     app.logger.debug(f'Listado de Personas: {personas}')
#     app.logger.debug(f'Total personas: {total_personas}')
#     return render_template('index.html', personas=personas, total_personas=total_personas)
#
#
# @app.route('/ver/<int:id>')
# def ver_detalle(id):
#     # Recuperar la persona según el Id
#     # persona = Persona.query.get(id)
#     persona = Persona.query.get_or_404(id)
#     app.logger.debug(f'Ver persona: {persona}')
#     return render_template('detalle.html', persona=persona)
#
#
# @app.route('/agregar', methods=['GET', 'POST'])
# def agregar():
#     persona = Persona()
#     personaForm = PersonaForm(obj=persona)
#     app.logger.debug('entre 0: ')
#     if request.method == 'POST':
#         app.logger.debug('entre : ')
#         app.logger.debug(personaForm.validate_on_submit())
#         if personaForm.validate_on_submit():
#             app.logger.debug('entre 1: ')
#             personaForm.populate_obj(persona)
#             app.logger.debug(f'Persona a insertar: {persona}')
#             # Insertamos el nuevo registro
#             db.session.add(persona)
#             db.session.commit()
#             return redirect(url_for('inicio'))
#     return render_template('agregar.html', forma=personaForm)
#
#
# @app.route('/editar/<int:id>', methods=['GET', 'POST'])
# def editar(id):
#     # Recupermos el objeto persona a editar
#     persona = Persona.query.get_or_404(id)
#     personaForm = PersonaForm(obj=persona)
#     if request.method == 'POST':
#         if personaForm.validate_on_submit():
#             personaForm.populate_obj(persona)
#             app.logger.debug(f'Persona a actualizar: {persona}')
#             db.session.commit()
#             return redirect(url_for('inicio'))
#     return render_template('editar.html', forma=personaForm)
#
#
# @app.route('/eliminar/<int:id>')
# def eliminar(id):
#     persona = Persona.query.get_or_404(id)
#     app.logger.debug(f'Persona a actualizar: {persona}')
#     db.session.delete(persona)
#     db.session.commit()
#     return redirect(url_for('inicio'))
