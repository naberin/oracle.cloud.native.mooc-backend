from src.resources.Database import Database


class CourseRepository(Database):

    def __init__(self):
        super(CourseRepository, self).__init__()

    def fetch_courses(self, with_search_criteria=None):
        if with_search_criteria:
            data = {"search_criteria": with_search_criteria}
            return self.fetch_all(query="""
                    select crs.* 
                    from OC_COURSES crs, OC_CATEGORIES cat
                    where 
                        crs.CATEGORY_ID = cat.CATEGORY_ID and
                        (
                        crs.COURSE_NAME like '%'||:search_criteria||'%' or
                        crs.COURSE_DESCRIPTION like '%'||:search_criteria||'%' or
                        cat.CATEGORY like '%'||:search_criteria||'%'
                        ) 
                    """, data=data)

        else:
            return self.fetch_all(query="""
                select * from OC_COURSES
            """)

