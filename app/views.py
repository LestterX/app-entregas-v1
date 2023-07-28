from flask import render_template, Blueprint, redirect, request,send_from_directory,jsonify
from .static.database.database_controller import add_onDatabase, get_db_connection, remove_fromDatabase, update_onDatabase
import json, os

views = Blueprint('views', __name__)

DIRETORIO_IMAGENS_PNG = 'E:\\AppEntregas\\AppEntregas\\app\\static\\downloads\\imagens_png'

@views.route('/', methods=['GET'])
def home():
    database = get_db_connection()
    ordens = database.execute('SELECT * FROM ordens').fetchall()
    status_pago = ''
    status_entregue = ''
    status_coletado = ''
    if request.method == 'GET':
        return render_template('home.html', ordens = ordens, status_pago = status_pago, status_entregue = status_entregue, status_coletado = status_coletado)
    database.close()
@views.route('/imprimir/<int:id>', methods=['GET'])
def imprimir(id):
    id_str = str(id)
    database = get_db_connection()
    ordem = database.execute('SELECT * FROM ordens WHERE id="'+id_str+'"').fetchall()
    print(ordem)
    if request.method == 'GET':
        return render_template('home_print.html', ordem = ordem[0])
    database.close()
    return redirect('/')
@views.route('/ordens-list', methods=['GET', 'POST'])
def json_ordens():
    if request.method == 'POST':
        database = get_db_connection()
        database.row_factory = None
        ordens = database.execute('SELECT * FROM ordens').fetchall()
        return json.dumps(ordens)
    else:
        return redirect('/')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@views.route('/nova-ordem')
def nova_ordem():
    database = get_db_connection()
    ordem_atual = database.execute('SELECT * FROM ordens ORDER BY Id DESC LIMIT 1').fetchall()
    database.close()
    return render_template('nova_ordem.html', ordem_atual = ordem_atual)
@views.route('/nova-ordem', methods=["POST"])
def salvar():   # ADICIONAR UM if methods == POST
    if request.method == 'POST': 
        nome_cliente = request.form["nome-cliente"]
        endereco_cliente = request.form["endereco-cliente"]
        telefone_cliente = request.form["telefone-cliente"]
        try:
            valor_servico = request.form["valor-servico"]
        except: # SÓ CAI AQUI QUANDO A OPÇÃO sem custo ESTIVER SELECIONADA
            valor_servico = '0,00'   # Para quando a opção SEM CUSTO estiver selecionada
        finally:
            forma_de_pagamento = request.form["forma-de-pagamento"]
            descricao_servico = request.form["descricao-servico"]
            add_onDatabase(nome_cliente, endereco_cliente, telefone_cliente, valor_servico, forma_de_pagamento, "false", "false", descricao_servico, "false")
            return redirect('/nova-ordem')
    else:
        return redirect('/nova-ordem')
@views.route('/fechar_ordem/<int:id>/atualizar_pagar', methods=['GET'])
def ocultar_ordem_pagar(id):
    if request.method == 'GET':
        database = get_db_connection()
        cursor = database.cursor()
        idStr = str(id)
        cursor.execute("UPDATE ordens SET pago = 'true' WHERE id='"+idStr+"'")
        database.commit()
        database.close()
        return redirect('/')
    return redirect('/nova_ordem')
@views.route('/fechar_ordem/<int:id>/atualizar_coletar', methods=['GET'])
def ocultar_ordem_coletar(id):
    if request.method == 'GET':
        database = get_db_connection()
        cursor = database.cursor()
        idStr = str(id)
        cursor.execute("UPDATE ordens SET coletado = 'true' WHERE id='"+idStr+"'")
        database.commit()
        database.close()
        return redirect('/')
    return redirect('/nova_ordem')
@views.route('/fechar_ordem/<int:id>/atualizar_entregar', methods=['GET'])
def ocultar_ordem_entregar(id):
    if request.method == 'GET':
        database = get_db_connection()
        cursor = database.cursor()
        idStr = str(id)
        cursor.execute("UPDATE ordens SET entregue='true' WHERE id='"+idStr+"'")
        database.commit()
        database.close()
        return redirect('/')
    return redirect('/nova_ordem')

@views.route('/ferramentas')
def ferramentas():
    return render_template('ferramentas.html')
@views.route('/ferramentas/gerenciador-de-links')
def ferramentas_gerenciador_links():
    database = get_db_connection()
    sites = database.execute('SELECT * FROM sites ORDER BY nome ASC').fetchall()
    return render_template('gerenciador_de_links.html', sites = sites)
@views.route('/ferramentas/gerenciador-de-links/editar')
def editar_sites():
    return render_template('ed_sites.html')
@views.route('/ferramentas/gerenciador-de-links/editar/action', methods = ['POST'])
def editar_sites_opp():
    nomeSite = request.form['nomesite']
    option = request.form['option']
    try: 
        linkSite = request.form['linksite']
    except: # SÓ CAI AQUI QUANDO A OPÇÃO remover ESTIVER SELECIONADA
        linkSite = ''   # Para quando a opção REMOVER estiver selecionada
    finally:
        if request.method == 'POST':
            if option == 'add': # Adicionar Site
                database = get_db_connection()
                cursor = database.cursor()
                cursor.execute("INSERT INTO sites (nome, link) VALUES ('"+nomeSite+"', '"+linkSite+"')")
                database.commit()
                database.close()
                return redirect('/ferramentas/gerenciador-de-links') 
            elif option == 'rem':   # Remover Site
                database = get_db_connection()
                cursor = database.cursor()
                cursor.execute("DELETE FROM sites WHERE nome='"+nomeSite+"'")
                database.commit()
                database.close()
                return redirect('/ferramentas/gerenciador-de-links') 
            else:
                return redirect('/ferramentas/gerenciador-de-links/editar')
        else:
            return redirect('/ferramentas/gerenciador-de-links/editar')
@views.route('/ferramentas/zap-sem-contato')
def zapSemContato():
    return render_template('zap_sem_contato.html')
@views.route('/ferramentas/icones-png', methods=['GET', 'POST'])
def icones_png():
    return render_template('icones_png.html')
@views.route('/ferramentas/icones-png/get-json', methods=['GET', 'POST'])
def listar_icones_png():
    imagens = []
    for nome_do_arquivo in os.listdir(DIRETORIO_IMAGENS_PNG):
        endereco_do_arquivo = os.path.join(DIRETORIO_IMAGENS_PNG, nome_do_arquivo)
        if(os.path.isfile(endereco_do_arquivo)):
            imagens.append(nome_do_arquivo)
    return jsonify(imagens)
@views.route('/ferramentas/icones-png/download/<nome_do_arquivo>', methods=['GET'])
def baixar_icone_png(nome_do_arquivo):
    return send_from_directory(DIRETORIO_IMAGENS_PNG, nome_do_arquivo, as_attachment=True)

@views.route('/consultar', methods=['GET'])
def consultar():
    database = get_db_connection()
    ordens = database.execute('SELECT * FROM ordens ORDER BY id DESC').fetchall()
    if request.method == 'GET':
        return render_template('consultar.html', ordens = ordens)
    database.close()
@views.route('/consultar/editar-ordem/<int:id>', methods=['GET', 'POST']) #Usar POST para atualizar valores
def editar_ordem(id):
    id_str = str(id)
    id_lista = id - 1
    database = get_db_connection()
    database.row_factory = None
    ordens = database.execute('SELECT * FROM ordens').fetchall()
    cliente = ordens[id_lista][1] # 0
    endereco = ordens[id_lista][2] # 1
    telefone = ordens[id_lista][3] # 2
    valor = ordens[id_lista][4] # 3
    forma_pagamento = ordens[id_lista][5] # 4
    pago = ordens[id_lista][6] # 5
    entregue = ordens[id_lista][7] # 6
    descricao = ordens[id_lista][8] # 7
    coletado = ordens[id_lista][9] # 8
    dados_form = [cliente, endereco, telefone, valor, forma_pagamento, pago, entregue, descricao, coletado]
    if request.method == 'GET':
        return render_template('editar_ordem.html', id = id_str, dados = dados_form)
    elif request.method == 'POST':
        nome_cliente = request.form["nome-cliente"]
        endereco_cliente = request.form["endereco-cliente"]
        telefone_cliente = request.form["telefone-cliente"]
        valor_servico = request.form["valor-servico"]
        forma_de_pagamento = request.form["forma-de-pagamento"]
        descricao_servico = request.form["descricao-servico"]
        pagamento_feito = request.form["servico-pago"]
        entrega_feita = request.form["servico-entregue"]
        coleta_feita = request.form['servico-coletado']
        update_onDatabase(id_str, nome_cliente, endereco_cliente, telefone_cliente, valor_servico, forma_de_pagamento, descricao_servico, pagamento_feito, entrega_feita, coleta_feita)
        return redirect('/consultar')
    database.close()
@views.route('/consultar/remover-ordem/<int:id>', methods=['GET'])
def remover_ordem(id):
    id_str = str(id)
    if request.method == 'GET':
        remove_fromDatabase(id_str)
        return redirect('/consultar')