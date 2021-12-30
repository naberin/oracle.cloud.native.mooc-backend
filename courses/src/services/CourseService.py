from src.utils.ApiResponse import ApiResponse
from src.repositories.CourseRepository import CourseRepository


class CourseService:

    @staticmethod
    def get_courses(search=None):
        courses = CourseRepository().fetch_courses(with_search_criteria=search)
        response = ApiResponse().set_payload(data={"items": courses, "count": len(courses)})
        return response.OK()
