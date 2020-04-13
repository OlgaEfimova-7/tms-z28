from flask_sqlalchemy import SQLAlchemy
from app import app
# import decimal


db = SQLAlchemy(app)


dish_foodstuff = db.Table('Dish_Foodstuff',
                db.Column('dish_id', db.Integer, db.ForeignKey('Dish.dish_id')),
                db.Column('foodstuff_id', db.Integer, db.ForeignKey('Foodstuff.foodstuff_id'))
                )


delivery_foodstuff = db.Table('Delivery_Foodstuff',
                db.Column('delivery_id', db.Integer, db.ForeignKey('Delivery.delivery_id')),
                db.Column('foodstuff_id', db.Integer, db.ForeignKey('Foodstuff.foodstuff_id'))
                )


order_dish = db.Table('Order_Dish',
                db.Column('order_id', db.Integer, db.ForeignKey('Order_in_restaurant.order_id')),
                db.Column('dish_id', db.Integer, db.ForeignKey('Dish.dish_id'))
                )


class Dish(db.Model):
    __tablename__ = 'Dish'
    dish_id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(100))
    price = db.Column(db.String(100))
    weight_grams = db.Column(db.Integer)
    foodstuffs = db.relationship('Foodstuff', secondary=dish_foodstuff, backref=db.backref('dishes'))

    def __init__(self, dish, price, weight_grams):
        self.dish = dish
        self.price = float(price)
        self.weight_grams = weight_grams


class Foodstuff(db.Model):
    __tablename__ = 'Foodstuff'
    foodstuff_id = db.Column('foodstuff_id', db.Integer, primary_key=True)
    name_of_foodstuff = db.Column(db.String(100))
    category = db.Column(db.String(100))

    def __init__(self, name_of_foodstuff, category):
        self.name_of_foodstuff = name_of_foodstuff
        self.category = category


class Waiter(db.Model):
    __tablename__ = 'Waiter'
    waiter_id = db.Column('waiter_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    address = db.Column(db.String(100))
    salary = db.Column(db.String(100))
    work_experience = db.Column(db.Integer)
    orders = db.relationship('Order', backref=db.backref('waiters'))

    def __init__(self, first_name, last_name, email, address, salary, work_experience):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.salary = salary
        self.work_experience = work_experience


class Order(db.Model):
    __tablename__ = 'Order_in_restaurant'
    order_id = db.Column('order_id', db.Integer, primary_key=True)
    order_date = db.Column(db.String(100))
    time_of_order = db.Column(db.String(100))
    order_price = db.Column(db.String(100))
    service_quality_assessment = db.Column(db.Integer)
    waiter_id = db.Column(db.Integer, db.ForeignKey('Waiter.waiter_id'))
    dishes = db.relationship('Dish', secondary=order_dish, backref=db.backref('orders'))

    def __init__(self, order_date, time_of_order, order_price, service_quality_assessment):
        self.order_date = order_date
        self.time_of_order = time_of_order
        self.order_price = order_price
        self.service_quality_assessment = service_quality_assessment


class Delivery(db.Model):
    __tablename__ = 'Delivery'
    delivery_id = db.Column('delivery_id', db.Integer, primary_key=True)
    delivery_date = db.Column(db.String(100))
    supplier = db.Column(db.String(100))
    cost_of_delivery = db.Column(db.String(100))
    delivery_on_time = db.Column(db.Boolean)
    foodstuffs = db.relationship('Foodstuff', secondary=delivery_foodstuff, backref=db.backref('deliveries'))

    def __init__(self, delivery_date, supplier, cost_of_delivery, delivery_on_time):
        self.delivery_date = delivery_date
        self.supplier = supplier
        self.cost_of_delivery = cost_of_delivery
        self.delivery_on_time = delivery_on_time


