from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

# Configuração inicial
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'chave-secreta-supersegura'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Modelo de usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Função de checagem de permissão
def checar_permissao(usuario, acao):
    permissoes = {
        "administrador": ["criar", "editar", "deletar", "ver"],
        "gerente": ["editar", "ver"],
        "usuario": ["ver"]
    }
    return acao in permissoes.get(usuario["role"], [])

# Decorator de permissão
def permissao_requerida(acao):
    def decorator(f):
        @wraps(f)
        @jwt_required()
        def wrapper(*args, **kwargs):
            usuario = get_jwt_identity()
            if not checar_permissao(usuario, acao):
                return jsonify({"msg": "Acesso negado"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Rota de login
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    usuario = User.query.filter_by(username=dados['username']).first()

    if usuario and check_password_hash(usuario.password, dados['password']):
        token = create_access_token(identity={
            "id": usuario.id,
            "username": usuario.username,
            "role": usuario.role
        })
        return jsonify(access_token=token)
    
    return jsonify({"msg": "Usuário ou senha inválidos"}), 401

# Rota protegida
@app.route('/admin/criar', methods=['POST'])
@permissao_requerida("criar")
def criar_item():
    return jsonify({"msg": "Item criado com sucesso"})

# Inicialização
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
