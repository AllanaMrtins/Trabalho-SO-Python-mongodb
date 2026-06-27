from flask import jsonify
from services.monitor_service import MonitorService

def listar_monitores():
    return jsonify(
        MonitorService.listar()
    )
