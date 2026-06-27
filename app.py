from flask import Flask, render_template

from routes.aluno_routes import aluno_bp
from routes.monitor_routes import monitor_bp
from routes.atendimento_routes import atendimento_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(aluno_bp)
app.register_blueprint(monitor_bp)
app.register_blueprint(atendimento_bp)
app.register_blueprint(dashboard_bp)


@app.route("/")
<<<<<<< HEAD
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/alunos")
def alunos():
    return render_template("alunos.html")

@app.route("/monitores")
def monitores():
    return render_template("monitores.html")

@app.route("/atendimentos")
def atendimentos():
    return render_template("atendimentos.html")

if __name__ == "__main__":
    app.run(debug=True)
=======
def home():
    return jsonify(
        {
            "Sistema": "SIGMON",
            "Descricao": "Sistema Integrado de Gestão de Monitorias",
            "Universidade": "UFPI",
            "Status": "online"
        }
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
>>>>>>> dc255fab67160dbae874a5c1c874c760ffd12b13
