from flask import Flask
from flask_bootstrap import Bootstrap
import controllers
import importlib
from pdb import set_trace

def create_app():
    app=Flask('Teste Flask')
    Bootstrap(app)
    registrar_blueprints(app)
    return app

def registrar_blueprints(app):
    for controller in controllers.__all__:
        globals()[controller] = importlib.import_module(f'controllers.{controller}')
        bp=globals()[controller].bp
        app.register_blueprint(bp)
        
    return app
