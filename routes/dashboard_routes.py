from flask import Blueprint
from controllers.dashboard_controller import (
    home,
    health,
    status_replica,
    login_controller  # <-- 1. Adicionado aqui na importação
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

dashboard_bp.route(
    "/",
    methods=["GET", "POST"]
)(home)

# <-- 2. ADICIONADO AQUI: Mapeia a URL /login para aceitar GET e POST
dashboard_bp.route(
    "/login",
    methods=["GET", "POST"]
)(login_controller)

dashboard_bp.route(
    "/health",
    methods=["GET", "POST"]
)(health)

dashboard_bp.route(
    "/replica-status",
    methods=["GET", "POST"]
)(status_replica)