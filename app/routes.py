from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
from app.controllers.car_controller import create_car, get_cars, get_car, update_car, delete_car    

bp = Blueprint('bp', __name__)

# User routes
@bp.route('/user', methods=['POST'])
def create():
    return create_user()

@bp.route('/user', methods=['GET'])
def get():
    return get_users()

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_by_id(user_id):
    return get_user(user_id)

@bp.route('/user/<int:user_id>', methods=['PUT'])   
def update(user_id):
    return update_user(user_id)

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    return delete_user(user_id)

# Car routes
@bp.route('/car', methods=['POST'])
def create__car():
    return create_car()

@bp.route('/car', methods=['GET'])
def get__cars():
    return get_cars()

@bp.route('/car/<int:car_id>', methods=['GET'])
def get__car(car_id):
    return get_car(car_id)

@bp.route('/car/<int:car_id>', methods=['PUT'])
def update__car(car_id):
    return update_car(car_id)

@bp.route('/car/<int:car_id>', methods=['DELETE'])
def delete__car(car_id):
    return delete_car(car_id)
