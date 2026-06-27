from flask import jsonify
from services.aluno_service import AlunoService

def listar_alunos():
    return jsonify(
    AlunoService.listar()
    )
