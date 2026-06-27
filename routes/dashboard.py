from flask import Blueprint
from controllers.dashboard_controller import (
    home,
    health,
    status_replica
    )

dashboard_bp = Blueprint(
    "dashboard",
    __name__
    )

dashboard_bp.route(
    "/",
    methods=["GET"]
    )(home)

dashboard_bp.route(
    "/health",
    methods=["GET"]
    )(health)

dashboard_bp.route(
    "/replica-status",
    methods=["GET"]
    )(status_replica)
