from flask import Flask
from src.controllers.HealthController import health

app = Flask(__name__)

app.register_blueprint(blueprint=health)

if __name__ == "__main__":
    app.run()
