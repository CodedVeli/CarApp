from flask import Blueprint, request, jsonify
from app import db
from app.models.car_model import Car
from sqlalchemy import exc
import logging

car = Blueprint('car', __name__)

@car.route('/car', methods=['POST'])
def create_car():
    try:
        make = request.json['make']
        model = request.json['model']
        year = request.json['year']
        user_id = request.json['user_id']
        car_instance = Car(make=make, model=model, year=year, user_id=user_id)
        db.session.add(car_instance)
        db.session.commit()
        return jsonify({'message': 'Car created successfully'}), 201
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Car already exists'}), 400
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Car could not be created'}), 500
    
@car.route('/car', methods=['GET'])
def get_cars():
    try:
        cars = Car.query.all()
        return jsonify([car.serialize() for car in cars]), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Cars could not be retrieved'}), 500
    
@car.route('/car/<int:car_id>', methods=['GET'])
def get_car(car_id):
    try:
        car = Car.query.get(car_id)
        return jsonify(car.serialize()), 200
    except AttributeError:
        return jsonify({'message': 'Car not found'}), 404
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Car could not be retrieved'}), 500
    
@car.route('/car/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    try:
        car = Car.query.get(car_id)
        make = request.json['make']
        model = request.json['model']
        year = request.json['year']
        user_id = request.json['user_id']
        car.make = make
        car.model = model
        car.year = year
        car.user_id = user_id
        db.session.commit()
        return jsonify({'message': 'Car updated successfully'}), 200
    except AttributeError:
        return jsonify({'message': 'Car not found'}), 404
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Car already exists'}), 400
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Car could not be updated'}), 500
    
@car.route('/car/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    try:
        car = Car.query.get(car_id)
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted successfully'}), 200
    except AttributeError:
        return jsonify({'message': 'Car not found'}), 404
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Car could not be deleted'}), 500
