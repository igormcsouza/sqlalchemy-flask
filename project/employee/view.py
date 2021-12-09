from flask import jsonify

from project.infra.database.repositories.employee import EmployeeRepository


repository = EmployeeRepository()


def index():
    all_employees = repository.get_all()
    return jsonify({"employees": [e.to_dict() for e in all_employees]}), 200

# post da criação do employee

# get para buscar employee pelo ID

# put da atualização do employee

# delete da deleção do employee