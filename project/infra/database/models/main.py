import os

from project.infra.database.main import Base, engine, DB_PATH
from project.infra.database.models.employee import EmployeeModel


def init_tables():
    if not os.path.isfile(DB_PATH):
        Base.metadata.create_all(engine)