from flask import Blueprint, jsonify, request
from server.models import db, Restaurant, RestaurantPizza

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    pizzas = [rp.pizza for rp in restaurant.restaurant_pizzas]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas]
    })

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
