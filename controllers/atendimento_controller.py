from flask import jsonify, request
from models.atendimento import Atendimento
from services.atendimento_service import AtendimentoService


def listar_atendimentos():
    return jsonify(AtendimentoService.listar())


def criar_atendimento():
    data = request.get_json()

    atendimento = Atendimento(
        aluno_matricula=data["aluno_matricula"],
        monitor_matricula=data["monitor_matricula"],
        disciplina=data["disciplina"],
        data=data["data"],
        horario=data["horario"],
        local=data["local"],
        descricao=data["descricao"],
        status=data["status"]
    )

    return jsonify(AtendimentoService.criar(atendimento))
