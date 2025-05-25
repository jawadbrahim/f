from flask import Blueprint
from project.features.food_category.controller import FoodController
from.blueprint import foods_bp
from .request_validator import request_validator
from ...decorators.validate import validate_schema
from ...decorators.request_limit import rate_limiter_decorator
from ...decorators.api_key import api_key_required
@foods_bp.route("/foods", methods=["POST"])
@api_key_required
@request_validator.validate_create_food()
def create_foods(validated_data):
    controller = FoodController()
    response = controller.create_foods(validated_data)
    return response, 201

@foods_bp.route("/foods/<int:food_id>", methods=["GET"])
@api_key_required
@rate_limiter_decorator()
def get_food(food_id):
    controller = FoodController()
    response = controller.get_foods(food_id)
    return response, 200

@foods_bp.route('/foods/group', methods=["GET"])
@api_key_required
@rate_limiter_decorator()
def get_grouped_foods():
    
    controller = FoodController()
    response = controller.get_grouped_foods()
    return response, 200
@foods_bp.route('/foods/<int:food_id>', methods=["PUT"])
@api_key_required
@request_validator.validate_update_foods()
def update_food(food_id, validated_data):
    controller = FoodController()
    response = controller.update_food(food_id, validated_data)
    return response, 200
@foods_bp.route('/food/<int:food_id>', methods=["DELETE"])
@api_key_required
def delete_food(food_id):
    controller = FoodController()
    response = controller.delete_food(food_id)
    return response, 200

@foods_bp.route('/foods/search/<string:title>', methods=["GET"])
@api_key_required
@rate_limiter_decorator()
def search_food(title):
    controller = FoodController()
    response = controller.search_food(title)
    return response, 200
@foods_bp.route("/favorite",methods=["POST"])
@api_key_required
@request_validator.validate_create_favorite()
def add_favorite(validated_data):
    controller=FoodController()
    response=controller.add_favorite_food(validated_data)
    return response,200
@foods_bp.route("/favorite/<uuid:user_id>", methods=["GET"])
@api_key_required
@rate_limiter_decorator()
def get_favorites(user_id):
    controller = FoodController()
    response = controller.get_favorite_foods(user_id)
    return response, 200
