from flask import jsonify, request
from services.aluno_service import AlunoService
from models.aluno import Aluno


def listar_alunos():
    return jsonify(AlunoService.listar())


def criar_aluno():
    data = request.get_json()

    aluno = Aluno(
        matricula=data["matricula"],
        nome=data["nome"],
        email=data["email"],
        curso=data["curso"],
        periodo=data["periodo"],
        disciplinas=data["disciplinas"]
    )

    result = AlunoService.criar(aluno)

    return jsonify(result)
