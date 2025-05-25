from .blueprints import firebase_bp
from .firebase_user import get_user_by_id,list_all_users,create_user,delete_user
from flask import jsonify
from .request_validator import request_validator
# from project.decorators.request_limit import rate_limiter_decorator
from project.features.food_category.data_access.orm_sqlalchemy import OrmSqlalchemyFoodCategory
@firebase_bp.route("/user/<user_id>",methods=["GET"])
def get_users(user_id):
    user=get_user_by_id(user_id)
    if user:
        return jsonify(user)
@firebase_bp.route("/firebase_users",methods=["GET"])
def get_list_users():
    users=list_all_users()
    return jsonify(users)
@firebase_bp.route("/create_user",methods=["POST"])
@request_validator.valdiate_create_user()
def create_users(validated_data):
    users=create_user(validated_data)
    return jsonify(users)
@firebase_bp.route("/delete/<user_id>",methods=["DELETE"])
def delete_users(user_id):
    users=delete_user(user_id)
    return jsonify(users)
@firebase_bp.route("/food/<food_id>", methods=["GET"])
# @rate_limiter_decorator()
def get_good(food_id):
    food_category = OrmSqlalchemyFoodCategory()
    food_data = food_category.get_food_by_id(food_id)
    
    if food_data:
        return jsonify(food_data)
    else:
        return jsonify({"error": "Food not found"}), 404
