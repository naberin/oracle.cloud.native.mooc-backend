from flask import Flask

from src.controllers.HealthController import health
from src.controllers.CategoryController import category

from src.resources.Pool import Pool

""" configure session pool """
pool = Pool().get()

app = Flask(__name__)
app.register_blueprint(category)
app.register_blueprint(health)


if __name__ == "__main__":
    """ run the flask application """
    app.run()
