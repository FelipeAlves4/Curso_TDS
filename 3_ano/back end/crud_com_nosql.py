from pymongo import MongoClient
from flask import Flask, jsonify, request

app = Flask(__name__)

# Conexão com o banco de dados MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
produtos_collection = db['produtos']

# Rota para adicionar um novo produto (CREATE)
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    produto_id = produtos_collection.insert_one(novo_produto).inserted_id
    return jsonify({"mensagem": "Produto adicionado com sucesso!", "id": str(produto_id)}), 201

# Rota para listar todos os produtos (READ)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = list(produtos_collection.find())
    for produto in produtos:
        produto['_id'] = str(produto['_id'])  # Converter ObjectId para string
    return jsonify(produtos)

# Rota para buscar um produto por ID (READ)
@app.route('/produtos/<id>', methods=['GET'])
def obter_produto(id):
    produto = produtos_collection.find_one({"_id": ObjectId(id)})
    if produto:
        produto['_id'] = str(produto['_id'])
        return jsonify(produto)
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404

# Rota para atualizar um produto (UPDATE)
@app.route('/produtos/<id>', methods=['PUT'])
def atualizar_produto(id):
    dados_atualizados = request.get_json()
    resultado = produtos_collection.update_one({"_id": ObjectId(id)}, {"$set": dados_atualizados})
    if resultado.matched_count > 0:
        return jsonify({"mensagem": "Produto atualizado com sucesso!"})
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404

# Rota para remover um produto (DELETE)
@app.route('/produtos/<id>', methods=['DELETE'])
def remover_produto(id):
    resultado = produtos_collection.delete_one({"_id": ObjectId(id)})
    if resultado.deleted_count > 0:
        return jsonify({"mensagem": "Produto removido com sucesso!"})
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)

