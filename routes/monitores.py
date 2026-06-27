from flask import Blueprint
from controllers.monitor_controller import listar_monitores

monitor_bp = Blueprint(
    "monitores",
    __name__
    )

monitor_bp.route(
    "/monitores",
    methods=["GET"]
    )(listar_monitores)
