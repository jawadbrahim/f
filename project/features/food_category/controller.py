from .food_service.factory import FactoryFoodService
from .data_access.factory import FactoryDataAccess
from .reponse_serializer.factory import FactoryReponseSerializer
from flask import jsonify
from .exceptions import FoodFailedToCreate,FoodNotExist,GroupedFoodIsEmpty,TitleNotFound
from project.redis.redis_cache import Rediscache
class FoodController:
    def __init__(self):
        self.data_access = FactoryDataAccess.build_object()
        self.food_service = FactoryFoodService.build_object(self.data_access)
        self.response_serializer = FactoryReponseSerializer.build_object()
        self.redis_cache=Rediscache()

    def create_foods(self, validated_data):
     try:
        food = self.food_service.create_foods(
            validated_data.category,
            validated_data.title,
            validated_data.description,
            validated_data.picture,
            validated_data.ingredients
        )
        self.data_access.commit()
        return self.response_serializer.serialize_create_food(food)
        
     except (FoodFailedToCreate, Exception) as e:
        
        return jsonify({"error": e.to_dict()})

    def get_foods(self, food_id):
        cache_key= f"food{food_id}"
        cached_foods_by_id=self.redis_cache.get_cache(cache_key)
        if cached_foods_by_id:
            return cached_foods_by_id

        try:
            food = self.food_service.get_foods_by_id(food_id)
            self.redis_cache.set_cache(cache_key,food)
            return food
        except (FoodNotExist,Exception) as e:
            return jsonify({"error":e.to_dict()})

    def get_grouped_foods(self,page=1,per_page=10):
        cache_key= "grouped_food"
        cached_grouped_food=self.redis_cache.get_cache(cache_key)
        if cached_grouped_food:
            return cached_grouped_food
        try:
            grouped_foods = self.food_service.get_food_by_group(page,per_page)
            self.redis_cache.set_cache(cache_key,grouped_foods)
            return grouped_foods
        except (GroupedFoodIsEmpty, Exception) as e:
            return jsonify({"error": e.to_dict()})

    def update_food(self, food_id, validated_data):
        try:
            updated_food = self.food_service.update_food(
                food_id,
                validated_data.category,
                validated_data.title,
                validated_data.description,
                validated_data.picture,
                validated_data.ingredients
            )
            self.data_access.commit()
            return self.response_serializer.serialize_update_food(updated_food)
        except (FoodNotExist, Exception) as e:
            return jsonify({"error": e.to_dict()})

    def delete_food(self, food_id):
        try:
            deleted_food = self.food_service.delete_food(food_id)
            
            self.data_access.commit()
            return self.response_serializer.serialize_delete_food(deleted_food)
        
        except (FoodNotExist,Exception) as e:
            return jsonify({"error": e.to_dict()})

    def search_food(self, title):
        cache_key=f"food:search:{title}"
        cache_data=self.redis_cache.get_cache(cache_key)
        if cache_data:
            return cache_data
        try:
            searched_food = self.food_service.search_food(title)
            self.redis_cache.set_cache(cache_key,searched_food)
            return searched_food
        except (TitleNotFound,Exception) as e:
            return jsonify({"error": e.to_dict()})
    def add_favorite_food(self,validated_data):
        try:
            favorite = self.food_service.add_favorite_food(validated_data.user_id, validated_data.food_id)
            self.data_access.commit()
            return self.response_serializer.serialize_favorite_created(favorite)
        except (FoodNotExist,Exception )as e:
            return jsonify({"error": e.to_dict()})
    def get_favorite_foods(self, user_id):
        try:
            favorite_foods = self.food_service.get_favorite_foods_by_user(user_id)
            return jsonify(favorite_foods)
        except (FoodNotExist,Exception) as e:
            return jsonify({"error":e.to_dict()})
