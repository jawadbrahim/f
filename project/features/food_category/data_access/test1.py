import unittest
from unittest.mock import patch
from project.features.food_category.data_access.orm_sqlalchemy import OrmSqlalchemyFoodCategory
from project.model.food_category import Foods
from helpers.app_creation import create_app
from database.postgres import db

class TestOrmSqlalchemyFoodCategory(unittest.TestCase):

    def setUp(self):
        """Set up a test app and database"""
        self.app = create_app(db)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        db.create_all()  # Create tables in the test database

    def tearDown(self):
        """Clean up after each test"""
        db.session.rollback()
        db.drop_all()  # Drop tables after each test
        self.app_context.pop()

    @patch('project.features.food_category.storage.google_storage.upload_to_gcs')
    def test_create_food_real(self, mock_upload):
        """Test food creation with real data, mocking external dependencies"""
        
        # Mock Google Cloud Storage upload function to return a test URL
        mock_upload.return_value = "https://test-bucket.com/images/a.jpg"

        orm = OrmSqlalchemyFoodCategory()
        category = "Dessert"
        title = "Chocolate Cake"
        description = "A delicious chocolate cake"
        picture = "a.jpg"
        ingredients = ["Flour", "Sugar", "Cocoa Powder", "Eggs"]

        # Create a food item
        food = orm.create_food(category, title, description, picture, ingredients)

        # Check if the food item was created
        self.assertIsNotNone(food)
        self.assertEqual(food.category, category)
        self.assertEqual(food.title, title)
        self.assertEqual(food.description, description)
        self.assertTrue(food.picture.startswith("https://"))  # Ensure picture URL is set
        self.assertEqual(food.ingredients, ingredients)

        # Verify that food exists in the database
        food_from_db = Foods.query.filter_by(title=title).first()
        self.assertIsNotNone(food_from_db)
        self.assertEqual(food_from_db.title, title)

if __name__ == "__main__":
    unittest.main()
