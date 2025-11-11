# Importa as bibliotecas necessárias do Flask
from flask import Flask, jsonify, request, render_template, redirect, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Banco de dados simples em memória (lista de dicionários)
# Cada produto possui id, nome, preço e quantidade
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00, "quantidade": 5},
    {"id": 2, "nome": "Mouse", "preco": 80.00, "quantidade": 30}
]

# Rota principal ("/") que mostra a página inicial
@app.route('/')
def index():
    # Renderiza o template index.html e passa a lista de produtos
    return render_template('index.html', produtos=produtos)

# Rota de API para listar todos os produtos em JSON
@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# 🔹 Rota de API para comprar um produto e reduzir sua quantidade
@app.route('/api/produtos/<int:id>/comprar', methods=['POST'])
def comprar_produto(id):
    # Busca o produto pelo ID
    produto = next((p for p in produtos if p['id'] == id), None)
    
    # Se não encontrar, retorna erro 404
    if not produto:
        return jsonify({"message": "Produto não encontrado"}), 404

    # Se a quantidade for 0 ou menor, retorna erro 400
    if produto['quantidade'] <= 0:
        return jsonify({"message": "Produto esgotado"}), 400

    # Reduz a quantidade em 1
    produto['quantidade'] -= 1

    # Retorna mensagem de sucesso e o produto atualizado
    return jsonify({"message": f"Compra registrada de {produto['nome']}", "produto": produto}), 200

# Rota para adicionar um novo produto via formulário HTML
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Pega os dados enviados pelo formulário
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        # Cria um novo produto com ID incremental
        novo = {"id": len(produtos) + 1, "nome": nome, "preco": preco, "quantidade": quantidade}
        # Adiciona na lista de produtos
        produtos.append(novo)
        # Redireciona para a página inicial
        return redirect(url_for('index'))
    # Se for GET, apenas renderiza o formulário
    return render_template('add.html')

# Rota para editar um produto existente via formulário HTML
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Busca o produto pelo ID
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    if request.method == 'POST':
        # Atualiza os dados do produto
        produto['nome'] = request.form['nome']
        produto['preco'] = float(request.form['preco'])
        produto['quantidade'] = int(request.form['quantidade'])
        # Redireciona para a página inicial
        return redirect(url_for('index'))
    # Se for GET, renderiza o formulário com os dados atuais do produto
    return render_template('edit.html', produto=produto)

# Rota para deletar um produto pelo ID
@app.route('/delete/<int:id>')
def delete(id):
    global produtos
    # Filtra a lista removendo o produto com o ID informado
    produtos = [p for p in produtos if p['id'] != id]
    # Redireciona para a página inicial
    return redirect(url_for('index'))

# Executa a aplicação na porta 5001 e acessível de qualquer IP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
