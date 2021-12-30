from src.utils.ApiResponse import ApiResponse
from src.repositories.CourseRepository import CourseRepository


class CourseService:

    @staticmethod
    def get_courses(category=None):
        courses = CourseRepository().fetch_courses()
        return ApiResponse().set_payload(data={"items": courses}).OK()
