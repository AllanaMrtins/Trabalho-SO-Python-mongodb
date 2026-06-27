from flask import jsonify
from database.replica_set import replica_status

def home():
    return jsonify(
    {
    "Sistema": "SIGMON",
    "Descricao": "Sistema Integrado de Gestão de Monitorias",
    "Universidade": "UFPI",
    "Status": "online"
    }
    )

def health():
    return jsonify(
    {
    "status": "ok"
    }
    )

def status_replica():
    return jsonify(
    replica_status()
    )
