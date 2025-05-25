from .controller import UserController
from .request_validator import request_validator
from project.decorators.token_required import token_required
# from project.decorators.request_limit import rate_limiter_decorator
from .blueprints import user_bp

@user_bp.route("/users",methods=["POST"])
@request_validator.validate_create_user()
@token_required
def create_user(validated_data,token_id):
    controller=UserController()
    response=controller.create_user(validated_data,token_id)
    return response,200

@user_bp.route("/users/<uuid:user_id>",methods=["GET"])
# @rate_limiter_decorator()
def get_users(user_id):
    controller=UserController()
    response=controller.get_user(user_id)
    return response,200
@user_bp.route("/users/delete/<uuid:user_id>",methods=["DELETE"])
def delete_user(user_id):
    controller=UserController()
    response=controller.delete_user(user_id)
    return response,201