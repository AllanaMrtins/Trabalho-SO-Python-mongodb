from services.monitor_service import MonitorService
from services.aluno_service import AlunoService
from services.atendimento_service import AtendimentoService

from flask import Flask, render_template, request, redirect, url_for

from routes.alunos_routes import aluno_bp
from routes.monitores_routes import monitor_bp
from routes.atendimentos_routes import atendimento_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

app.register_blueprint(aluno_bp)
app.register_blueprint(monitor_bp)
app.register_blueprint(atendimento_bp)
app.register_blueprint(dashboard_bp, url_prefix="/api")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Pega os dados digitados na tela (para usar com MongoDB depois)
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        
        # Redireciona o usuário para a tela do Dashboard após o login com sucesso!
        return redirect(url_for("dashboard_page"))
        
    return render_template("login.html")


@app.route("/dashboard-page")
def dashboard_page():
    dados = {
        "total_alunos": AlunoService.contar(),
        "total_monitores": MonitorService.contar(),
        "total_atendimentos": AtendimentoService.contar()
    }

    return render_template(
        "dashboard.html",
        dados=dados
    )

@app.route("/alunos-page", methods=["GET", "POST"])
def alunos_page():
    if request.method == "POST":
        # Captura todos os campos enviados pelo formulário
        dados_aluno = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "curso": request.form.get("curso"),
            "periodo": int(request.form.get("periodo")), 
            "disciplinas": request.form.get("disciplinas")
        }
        
        # Envia o dicionário completo para o banco
        AlunoService.salvar(dados_aluno)
        return redirect(url_for("alunos_page"))
        
    lista_de_alunos = AlunoService.listar()
    return render_template("alunos.html", alunos=lista_de_alunos)



@app.route("/monitores-page", methods=["GET", "POST"])
def monitores_page():
    if request.method == "POST":
        # Captura os campos do formulário de monitores
        dados_monitor = {
            "nome": request.form.get("nome"),
            "disciplina": request.form.get("disciplina"),
            "curso": request.form.get("curso"),
            "periodo": int(request.form.get("periodo")), # Converte para número inteiro
            "docente": request.form.get("docente")
        }
        
        # Envia para salvar no MongoDB
        MonitorService.salvar(dados_monitor)
        return redirect(url_for("monitores_page"))
        
    lista_de_monitores = MonitorService.listar()
    return render_template("monitores.html", monitores=lista_de_monitores)



@app.route("/atendimentos-page", methods=["GET", "POST"])
def atendimentos_page():
    if request.method == "POST":
        disciplina_escolhida = request.form.get("disciplina")
        
        # Busca automatizada de quem é o monitor
        monitor_encontrado = MonitorService.buscar_por_disciplina(disciplina_escolhida)
        
        # Se achar o monitor, pega o nome dele. Se não achar, coloca um texto padrão.
        nome_monitor = monitor_encontrado.get("nome") if monitor_encontrado else "A definir (Sem monitor ativo)"
        
        dados_atendimento = {
            "tipo": request.form.get("tipo"),
            "disciplina": disciplina_escolhida,
            "descricao": request.form.get("descricao"),
            "monitor_responsavel": nome_monitor  # <-- GRAVAÇÃO AUTOMÁTICA NO BANCO
        }
        
        AtendimentoService.salvar(dados_atendimento)
        return redirect(url_for("atendimentos_page"))
        
    lista_de_atendimentos = AtendimentoService.listar()
    return render_template("atendimentos.html", atendimentos=lista_de_atendimentos)



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
