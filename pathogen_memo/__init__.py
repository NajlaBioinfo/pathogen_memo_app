"""
Pathogen Memo APP
by : NajlaBioinfo
Dec 2019

Script: Create_app.py
"""
#Import flask dependencies
from flask import Flask, jsonify, redirect, render_template, flash, Blueprint, request, session, url_for, make_response, send_from_directory

#Import commands
from .commands import create_tables

#Import extensions
from .extensions import db, login_manager

#Import model
from .models import User, Pathogen

#Import swagger/ bootstrap
from flask_swagger_ui import get_swaggerui_blueprint
from flask_bootstrap import Bootstrap


#__ local/perso modules
from .routes import request_api
from .views.index import indexv
from .views.about import aboutv

from .views.cud import cudv
from .views.newpathogen import newpathv
from .views.update import updatev
from .views.delete import deletev

def create_app(config_file='settings.py'):
    """
    Launch script: create pathogen-memo-app
    """
    app = Flask(__name__,
            static_folder='static',
            static_url_path= '/static',
            template_folder='templates')

    #SETTINGS
    app.config.from_pyfile(config_file)

    #INITIALIZATIONS
 
    #__DB INIT
    db.init_app(app)
    #COMMANDS CALL
    app.cli.add_command(create_tables)
    
    #__LOGIN-MANGER INIT
    login_manager.init_app(app)



    ###  __ Swagger settings __ [BEGIN] ###
    ## Init routes
    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static',path)

    SWAGGER_URL ='/swagger'
    API_URL='/static/swaggers/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Pathogen-Memo Python Flask Rest"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    ###  __ Swagger settings __ [END] ###



    ###  __ ERROR ROUTES SETTINGS __ [BEGIN] ###
    app.register_blueprint(request_api.get_blueprint())
    @app.errorhandler(400)
    def handle_400_error(_error):
        """Return a http 400 error to client"""
        return make_response(jsonify({'error': 'Misunderstood'}), 400)

    @app.errorhandler(401)
    def handle_401_error(_error):
        """Return a http 401 error to client"""
        return make_response(jsonify({'error': 'Unauthorised'}), 401)

    @app.errorhandler(404)
    def handle_404_error(_error):
        """Return a http 404 error to client"""
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.errorhandler(500)
    def handle_500_error(_error):
        """Return a http 500 error to client"""
        return make_response(jsonify({'error': 'Server error'}), 500)
    ###  __ ERROR ROUTES SETTINGS __ [END] ###



    #VIEWS CALL - login/login manager views
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        """Check if user is logged-in on every page load."""
        if user_id is not None:
            return User.query.get(user_id)
        return None

    @login_manager.unauthorized_handler
    def unauthorized():
        """Redirect unauthorized users to Login page."""
        flash('You must be logged in to view that page.')
        return redirect(url_for('auth_bp.login_page'))


    ###  __ VIEWS SETTINGS __ [BEGIN] ###
    bootstrap = Bootstrap(app)
    app.register_blueprint(indexv)
    app.register_blueprint(aboutv)
    app.register_blueprint(cudv)
    app.register_blueprint(newpathv)
    app.register_blueprint(updatev)
    app.register_blueprint(deletev)
    ###  __ VIEWS SETTINGS __ [END] ###

    #Call singup /auth views
    from .routes.signup import auth_bp
    from .views.dashboard import main_bp
    from .views.barplota import barplotav
    from .views.barplotb import barplotbv
    from .views.barplotc import barplotcv
    from .views.barplotd import barplotdv


    with app.app_context():
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)
        app.register_blueprint(barplotav)
        app.register_blueprint(barplotbv)
        app.register_blueprint(barplotcv)
        app.register_blueprint(barplotdv)


    #COMMANDS CALL
    #app.cli.add_command(create_tables)

    return app
