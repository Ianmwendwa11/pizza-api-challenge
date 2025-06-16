from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
