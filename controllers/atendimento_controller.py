from flask import jsonify
from services.atendimento_service import AtendimentoService

def listar_atendimentos():
    return jsonify(
    AtendimentoService.listar()
    )
