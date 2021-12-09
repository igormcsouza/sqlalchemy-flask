from typing import List

from project.infra.database.main import DBSession
from project.infra.database.models.employee import EmployeeModel


class EmployeeRepository:

    def __init__(self):
        self.session = DBSession()

    def get_all(self) -> List[EmployeeModel]:
        employees = self.session.query(EmployeeModel)

        return employees

    def create(self, employee: EmployeeModel) -> None:
        self.session.add(employee)
        self.session.commit()

    def get(self, id: int) -> EmployeeModel:
        employee = self.session\
            .query(EmployeeModel)\
            .filter(EmployeeModel.id == id)\
            .one()

        return employee

    # atualizar

    # deletar