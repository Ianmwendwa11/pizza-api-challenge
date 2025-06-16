from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Domino's", address="123 Main St")
    r2 = Restaurant(name="Pizza Inn", address="456 Elm St")

    p1 = Pizza(name="Margherita", ingredients="Cheese, Tomato")
    p2 = Pizza(name="Pepperoni", ingredients="Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza=p1, restaurant=r1)
    rp2 = RestaurantPizza(price=12, pizza=p2, restaurant=r2)

    db.session.add_all([rp1, rp2])
    db.session.commit()
