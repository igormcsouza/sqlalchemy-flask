from flask import Flask

from project import employee
from project.infra import database


app = Flask(__name__)


# Initialize the blueprint
employee.init_app(app)

# Initialize Tables
database.init_tables()
