from flask import Blueprint
from controllers.atendimento_controller import (
    listar_atendimentos,
    criar_atendimento
)

atendimento_bp = Blueprint("atendimentos", __name__)

atendimento_bp.route("/atendimentos", methods=["GET"])(listar_atendimentos)
atendimento_bp.route("/atendimentos", methods=["POST"])(criar_atendimento)
