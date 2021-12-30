from src.utils.ApiResponse import ApiResponse


class HealthService:

    def get_health(self):
        return ApiResponse().set_payload(data={"status": "UP"}).OK()
