from flask import Flask, request, redirect

app = Flask(__name__)

lista_tarefas = [
    {'id': 1, 'descricao': 'Comprar pão'},
    {'id': 2, 'descricao': 'Fazer exercícios'},
    {'id': 3, 'descricao': 'Ler um livro'},
    {'id': 4, 'descricao': 'Assistir um filme'},
    {'id': 5, 'descricao': 'Cozinhar o jantar'},
]

@app.route('/')
def index():
    return 'Bem-vindo ao meu aplicativo de lista de tarefas!'

@app.route('/tarefas')
def tarefas():
    html = '<ul>'
    for tarefa in lista_tarefas:
        html += f'<li>{tarefa["descricao"]} <a href="/remover-tarefa/{tarefa["id"]}">remover</a></li>'
    html += '</ul>'

    html += '<a href="/adicionar-tarefa">Adicionar tarefa</a>'

    return html


@app.route('/adicionar-tarefa')
def adicionar_tarefa():
    html = '''
        <form method="POST" action="/salvar-tarefa">
            <label for="descricao">Descrição da tarefa:</label>
            <input type="text" id="descricao" name="descricao">
            <button type="submit">Adicionar tarefa</button>
        </form>
    '''

    return html


@app.route('/salvar-tarefa', methods=['POST'])
def salvar_tarefa():
    descricao = request.form['descricao']
    nova_tarefa = {'id': len(lista_tarefas) + 1, 'descricao': descricao}
    lista_tarefas.append(nova_tarefa)

    return redirect('/tarefas')


@app.route('/remover-tarefa/<int:id>')
def remover_tarefa(id):
    global lista_tarefas
    lista_tarefas = [tarefa for tarefa in lista_tarefas if tarefa['id'] != id]
    return redirect('/tarefas')


if __name__ == '__main__':
    app.run()

#http://localhost:5000/
#http://localhost:5000/tarefas
#http://localhost:5000/adicionar-tarefa