from functools import wraps
from flask import jsonify, request
from project.redis.redis_limiter import get_rate_limiter
from firebase_admin import auth
limiter, rate_limit = get_rate_limiter(limit=10, per_minute=True)

def rate_limiter_decorator():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_id = request.headers.get("user_id")
            if not user_id:
                return jsonify({"error": "User ID is missing in the request headers"}), 400
            user = auth.get_user(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404
            if not limiter.hit(rate_limit, user_id):
                return jsonify({"error": "Too many requests"}), 429
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
