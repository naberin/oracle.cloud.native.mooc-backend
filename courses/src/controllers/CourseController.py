from flask import Blueprint, request
from src.services.CourseService import CourseService

courses = Blueprint("courses", __name__, url_prefix="/api")


@courses.route("/course", methods=["GET"])
def get_course():
    category = request.args.get(key="category")

    return CourseService().get_courses(category=category)
