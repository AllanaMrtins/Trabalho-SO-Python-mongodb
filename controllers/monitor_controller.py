from flask import jsonify, request
from models.monitor import Monitor
from services.monitor_service import MonitorService


def listar_monitores():
    return jsonify(MonitorService.listar())


def criar_monitor():
    data = request.get_json()

    monitor = Monitor(
        matricula=data["matricula"],
        nome=data["nome"],
        email=data["email"],
        disciplina=data["disciplina"],
        horario=data["horario"]
    )

    return jsonify(MonitorService.criar(monitor))
