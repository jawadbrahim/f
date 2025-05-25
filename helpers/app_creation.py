from flask import Flask,send_from_directory
from project.config.development import Development
from project.features.firebase.firebase_init import init_credential
from flask_swagger_ui import get_swaggerui_blueprint
from project.decorators.api_key import api_key_required
def create_app(db):
    app = Flask(__name__)
    
    app.config.from_object(Development)
    
    init_credential()
    # print(f"static_folder: {app.static_folder}")
    db.init_app(app)
    SWAGGER_URL = '/swagger'
    API_DOCS_PATH = '/static/swagger.yaml'

    swaggerui_blueprint = get_swaggerui_blueprint( 
    SWAGGER_URL,
    API_DOCS_PATH,
    config={ 
        'app_name': "Food Category API",
       
    }
)
    @app.route('/static/swagger.yaml')
    def swagger_yaml():
     return send_from_directory('static', 'swagger.yaml')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    
    
    with app.app_context():
        from project.features.food_category.route import foods_bp
        from project.features.user.route import user_bp
        from project.features.authentication.routes import auth_bp
        from project.features.chat.route import chat_bp
        from project.features.review.route import review_bp
        from project.features.firebase.routes import firebase_bp
        
        app.register_blueprint(foods_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(chat_bp)
        app.register_blueprint(review_bp)
        app.register_blueprint(firebase_bp)
        
        
        
        # print(app.url_map)
    
    return app
