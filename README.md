 README.md — Pizza Restaurant API
 Project Setup
Clone the repository

bash
Copy
Edit
git clone <Pizza-api-challenge>
cd pizza-api-challenge
Set up environment

bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
Database setup

bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seeding the database
Add data to server/seed.py and run:

bash
Copy
Edit
python server/seed.py


Routes Summary

/restaurants
GET: Returns all restaurants.


/restaurants/<int:id>
GET: Returns restaurant details and pizzas.


DELETE: Deletes a restaurant and all associated restaurant-pizzas.


/pizzas
GET: Returns all pizzas.


/restaurant_pizzas
POST: Creates a new restaurant-pizza relationship.


Sample Requests

http
Copy
Edit
GET /restaurants
200 OK
[
  {
    "id": 1,
    "name": "Mario's",
    "address": "123 Pizza St"
  }
]
http
Copy
Edit
POST /restaurant_pizzas
Content-Type: application/json
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}
201 CREATED
{
  "id": 4,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "address2"
  }
}


Validation Rules

price must be between 1 and 30

restaurant_id and pizza_id must reference valid records


Postman Usage

Open Postman.

Import challenge-1-pizzas.postman_collection.json.

Test all routes directly.