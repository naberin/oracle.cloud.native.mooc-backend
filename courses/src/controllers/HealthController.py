from src.services.HealthService import HealthService
from flask import Blueprint

health = Blueprint("health", __name__, url_prefix="/api")


@health.route("/health", methods=["GET"])
def get_health():
    return HealthService().get_health()
