from src.resources.Database import Database


class CategoryRepository(Database):

    def __init__(self):
        super(CategoryRepository, self).__init__()

    def fetch_category(self):
        return self.fetch_all(query="""select * from OC_CATEGORIES""")

