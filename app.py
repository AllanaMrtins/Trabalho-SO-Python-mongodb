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
def login():
    return render_template("login.html")


@app.route("/dashboard-page")
def dashboard_page():
    return render_template("dashboard.html")


@app.route("/alunos-page")
def alunos_page():
    return render_template("alunos.html")


@app.route("/monitores-page")
def monitores_page():
    return render_template("monitores.html")


@app.route("/atendimentos-page")
def atendimentos_page():
    return render_template("atendimentos.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
