from flask import Blueprint, request, jsonify
from app import db
from app.models.user_model import User
from sqlalchemy import exc
import logging

logging.basicConfig(level=logging.INFO)



def create_user():
    try:
        username = request.json['username']
        password = request.json['password']
        usertype = request.json['usertype']
        user = User(username=username, password=password, usertype=usertype)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User already exists'}), 400
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'User could not be created'}), 500
    
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'Users could not be retrieved'}), 500
    

def get_user(user_id):
    try:
        user = User.query.get(user_id)
        return jsonify(user.serialize()), 200
    except AttributeError:
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'User could not be retrieved'}), 500
    


def update_user(user_id):
    try:
        user = User.query.get(user_id)
        username = request.json['username']
        password = request.json['password']
        usertype = request.json['usertype']
        user.username = username
        user.password = password
        user.usertype = usertype
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    except AttributeError:
        return jsonify({'message': 'User not found'}), 404
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User already exists'}), 400
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'User could not be updated'}), 500
    

def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except AttributeError:
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        logging.error(e)
        return jsonify({'message': 'User could not be deleted'}), 500
    

    