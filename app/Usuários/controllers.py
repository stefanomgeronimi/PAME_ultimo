from ..extensions import Blueprint, request, jsonify, db
from app.Usuários.model import Usuarios

usuario_api = Blueprint('usuario_api', __name__)

@pessoa_api.route('/usuarios,', methods=['GET'])
def index():
    if request.method == 'GET':
        usuarios = Usuarios.object.all()
        return jsonify([usuario.json() for usuario in usuarios])

    if request.method == 'POST':
        data = request.json

        nome_de_usuario = data.get('nome')
        idade = data.get('idade')
        data_de_inscricao = data.get('data')
        n_de_posts = data.get('n_posts')

        usuario = Usuarios(nome_de_usuario=nome_de_usuario, idade=idade, data_de_inscricao=data_de_inscricao,
        n_de_posts=n_de_posts)

    db.session.add(usuario)
    db.session.commit()

    return usuario.json(), 200