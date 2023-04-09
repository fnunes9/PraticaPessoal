from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        'id': 1,
        'titulo': 'Invocação do Mal',
        'streamming': 'netflix'
    },
    {
        'id': 2,
        'titulo': 'Pantera negra',
        'streamming': 'disney+'
    },
    {
        'id': 3,
        'titulo': 'Interestellar',
        'streamming': 'prime'
    },
    {
        'id': 4,
        'titulo': 'A culpa e das estrelas',
        'streamming': 'netflix'
    }
]

#Criar uma função para cada endpoint que quer oferecer.
@app.route('/filmes', methods=['GET'])
def obter_filmes():
    return jsonify(filmes)
#Consultar id
@app.route('/filmes/<int:id>',methods=['GET']) # type: ignore
def obter_filmes_por_id(id):
    for filme in filmes:
      if filme.get('id')== id:
        return jsonify(filme)

#editar filme por id
@app.route('/filmes/<int:id>',methods=['PUT']) # type: ignore
def editar_filmes_por_id(id):
   filme_alterado= request.get_json()
   for indice,filme in enumerate(filmes):
      if filme.get('id')==id:
        filmes[indice].update(filme_alterado)
        return jsonify(filmes[indice])

#criar
@app.route('/filmes',methods=['POST'])
def criar_novo_filme():
   novo_filme=request.get_json()
   filmes.append(novo_filme)

   return jsonify(filmes)
   
#EXCLUIR
@app.route('/filmes/<int:id>',methods=['DELETE']) # type: ignore
def exluir_filmes(id):   
   for indice, filme in enumerate(filmes):
      if filme.get('id')==id:
         del filmes[indice]
         return jsonify(filmes)
     
app.run(port=5000,host='localhost',debug=True)



