from src.resources.Database import Database


class CourseRepository(Database):

    def __init__(self):
        super(CourseRepository, self).__init__()

    def fetch_courses(self, using_category=None):
        return self.fetch_all(query="""select * from OC_COURSES""")

