from flask import Blueprint
from controllers.aluno_controller import listar_alunos,criar_aluno

aluno_bp = Blueprint("alunos",__name__)

aluno_bp.route("/alunos",methods=["GET"])(listar_alunos)
aluno_bp.route("/alunos", methods=["POST"])(criar_aluno)
