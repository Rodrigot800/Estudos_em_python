# Importa as bibliotecas necessárias do Flask
from flask import Flask, request, jsonify, render_template

# Cria a aplicação Flask
app = Flask(__name__)

# Lista em memória para armazenar as vendas
vendas = []

# Rota de API para registrar uma nova venda (POST)
@app.route('/api/vendas', methods=['POST'])
def registrar_venda():
    # Pega os dados da venda enviados em JSON no corpo da requisição
    produto = request.json
    # Adiciona a venda na lista em memória
    vendas.append(produto)
    # Retorna uma mensagem de sucesso com status 201 (Criado)
    return jsonify({"message": "Venda registrada"}), 201

# Rota de API para listar todas as vendas (GET)
@app.route('/api/vendas', methods=['GET'])
def listar_vendas():
    # Retorna todas as vendas em formato JSON
    return jsonify(vendas)

# Rota principal que mostra a página de relatório
@app.route('/')
def pagina_relatorio():
    # Renderiza o template relatorio.html
    return render_template('relatorio.html')

# Executa a aplicação Flask na porta 5002 e acessível de qualquer IP
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
