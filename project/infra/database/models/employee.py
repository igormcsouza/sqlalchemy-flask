from sqlalchemy import Column, Integer, String

from project.infra.database.main import Base


class EmployeeModel(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }