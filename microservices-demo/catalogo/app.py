# Importa as bibliotecas necessárias do Flask
from flask import Flask, render_template, jsonify
# Importa a biblioteca requests para fazer requisições HTTP para outros serviços
import requests

# Cria a aplicação Flask
app = Flask(__name__)

# URLs dos serviços externos (microserviços)
ESTOQUE_URL = "http://estoque:5001/api/produtos"   # Serviço de estoque
RELATORIO_URL = "http://relatorios:5002/api/vendas"  # Serviço de relatórios

# Rota principal que serve a página inicial
@app.route('/')
def index():
    # Renderiza o template HTML 'index.html'
    return render_template('index.html')

# Rota que lista todos os produtos 
@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    try:
        # Faz uma requisição GET para o serviço de estoque para pegar os produtos
        res = requests.get(ESTOQUE_URL, timeout=3)  # timeout de 3 segundos
        produtos = res.json()  # Converte a resposta JSON em lista/dicionário Python
    except Exception as e:
        # Em caso de erro, exibe no console e retorna lista vazia
        print("Erro ao acessar o estoque:", e)
        produtos = []
    # Retorna os produtos em formato JSON
    return jsonify(produtos)

# Rota para realizar a compra de um produto específico pelo seu ID
@app.route('/api/comprar/<int:id>', methods=['POST'])
def comprar_produto(id):
    try:
        # 🔹 Busca todos os produtos no estoque
        res = requests.get(ESTOQUE_URL)
        produtos = res.json()
        # Procura o produto com o ID informado
        produto = next((p for p in produtos if p['id'] == id), None)

        # Se o produto não existir, retorna erro 404
        if not produto:
            return jsonify({"message": "Produto não encontrado"}), 404
        # Se a quantidade do produto for 0 ou menor, retorna erro 400
        if produto['quantidade'] <= 0:
            return jsonify({"message": "Produto esgotado"}), 400

        # 🔹 Faz requisição POST no serviço de estoque para reduzir a quantidade
        estoque_res = requests.post(f"http://estoque:5001/api/produtos/{id}/comprar")
        # Se a requisição falhar, retorna erro 500
        if estoque_res.status_code != 200:
            return jsonify({"message": "Falha ao atualizar estoque"}), 500

        # 🔹 Atualiza a quantidade localmente (pra refletir sem precisar recarregar a página)
        produto['quantidade'] -= 1

        # 🔹 Prepara os dados da venda para enviar ao serviço de relatórios
        venda = {
            "nome": produto['nome'],
            "preco": produto['preco'],
            "quantidade": 1
        }
        try:
            # Envia a venda para o serviço de relatórios
            requests.post(RELATORIO_URL, json=venda)
        except Exception as e:
            # Se falhar, apenas registra o erro no console (não interrompe a compra)
            print("Erro ao enviar venda para relatórios:", e)

        # Retorna sucesso para o frontend com os detalhes do produto comprado
        return jsonify({
            "message": f"Compra de {produto['nome']} registrada com sucesso!",
            "produto": produto
        })

    except Exception as e:
        # Captura qualquer outro erro inesperado e retorna erro 500
        print("Erro ao processar compra:", e)
        return jsonify({"message": "Erro ao processar compra"}), 500

# Inicia a aplicação Flask na porta 5000 e acessível de qualquer IP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
