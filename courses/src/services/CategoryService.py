from src.utils.ApiResponse import ApiResponse
from src.repositories.CategoryRepository import CategoryRepository


class CategoryService:

    @staticmethod
    def get_categories():
        categories = CategoryRepository().fetch_category()

        response = ApiResponse().set_payload(data={"items": categories})
        return response.OK()
