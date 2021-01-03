from flask import Blueprint,render_template

bp=Blueprint('Teste Flask',__name__,template_folder='templates')

@bp.route('/')
def index():
    contexto={
        'mensagem': 'Hello World'
    }
    return render_template('index.html',**contexto)
