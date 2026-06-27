from flask import Flask, jsonify

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
