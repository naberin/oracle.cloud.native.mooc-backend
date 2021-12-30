from flask import Blueprint

from src.services.CategoryService import CategoryService

category = Blueprint("category", __name__)


@category.route("/api/category", methods=["GET"])
def get_category():
    return CategoryService.get_categories()
