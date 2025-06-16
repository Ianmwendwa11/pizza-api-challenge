from flask import Blueprint, request, jsonify
from server.models import db, RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data.get("price"))
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        pizza_id = int(data.get("pizza_id"))
        restaurant_id = int(data.get("restaurant_id"))
    except (TypeError, ValueError) as e:
        return jsonify({"errors": [str(e)]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201
