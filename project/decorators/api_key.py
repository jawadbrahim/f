from functools import wraps
from flask import request, jsonify
import os

def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
       
        API_KEY = os.getenv("API_KEY")
        api_key = request.headers.get('api_key') or request.args.get('api_key')
        if not api_key or api_key != API_KEY:
            return jsonify({"error": "Unauthorized. Invalid or missing API key."}), 401
        
        return f(*args, **kwargs)
    return decorated_function
