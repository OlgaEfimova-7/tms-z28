from flask import render_template, redirect, url_for, request
from app import app
from ORM import Dish, db, Waiter, Foodstuff, Delivery, Order


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/delivery')
def delivery():
    return render_template('delivery.html', a=Delivery.query.filter_by().all())


@app.route('/delivery/<value>')
def delivery_by_id(value):
    return render_template('delivery_by_id.html', a=Delivery.query.get(value))


@app.route('/delivery/<value>/delete')
def delivery_delete(value):
    Delivery.query.filter(Delivery.delivery_id == value).delete()
    db.session.commit()
    return redirect(url_for('delivery'))


@app.route('/delivery/<value>/change')
def delivery_change(value):
    return render_template('delivery_change.html', a=Delivery.query.get(value))


@app.route('/delivery/<value>/change/success', methods=['POST'])
def delivery_change_success(value):
    new_supplier = request.form['supplier']
    new_cost_of_delivery = request.form['cost_of_delivery']
    new_date_of_delivery = request.form['delivery_date']
    Delivery.query.filter(Delivery.delivery_id == value).update({'supplier': new_supplier,
                                                                 'cost_of_delivery': new_cost_of_delivery,
                                                                 'delivery_date': new_date_of_delivery})
    db.session.commit()
    return redirect(url_for('delivery_by_id', value=value))


@app.route('/dish')
def dish():
    return render_template('dish.html', a=Dish.query.filter_by().all())


@app.route('/dish/<value>')
def dish_by_id(value):
    return render_template('dish-by_id.html', a=Dish.query.get(value))


@app.route('/dish/<value>/delete')
def dish_delete(value):
    Dish.query.filter(Dish.dish_id == value).delete()
    db.session.commit()
    return redirect(url_for('dish'))


@app.route('/dish/<value>/change')
def dish_change(value):
    return render_template('dish_change.html', a=Dish.query.get(value))


@app.route('/dish/<value>/change/success', methods=['POST'])
def dish_change_success(value):
    new_dish = request.form['dish']
    new_price = request.form['price']
    new_weight = request.form['weight']
    Dish.query.filter(Dish.dish_id == value).update({'dish': new_dish, 'price': new_price,
                                                     'weight_grams': new_weight})
    db.session.commit()
    return redirect(url_for('dish_by_id', value=value))


@app.route('/foodstuff')
def foodstuff():
    return render_template('foodstuff.html', a=Foodstuff.query.filter_by().all())


@app.route('/foodstuff/<value>')
def foodstuff_by_id(value):
    return render_template('foodstuff_by_id.html', a=Foodstuff.query.get(value))


@app.route('/foodstuff/<value>/delete')
def foodstuff_delete(value):
    Foodstuff.query.filter(Foodstuff.foodstuff_id == value).delete()
    db.session.commit()
    return redirect(url_for('foodstuff'))


@app.route('/foodstuff/<value>/change')
def foodstuff_change(value):
    return render_template('foodstuff_change.html', a=Foodstuff.query.get(value))


@app.route('/foodstuff/<value>/change/success', methods=['POST'])
def foodstuff_change_success(value):
    new_name_of_foodstuff = request.form['name_of_foodstuff']
    new_category = request.form['category']
    Foodstuff.query.filter(Foodstuff.foodstuff_id == value).update({'name_of_foodstuff': new_name_of_foodstuff,
                                                                    'category': new_category})
    db.session.commit()
    return redirect(url_for('foodstuff_by_id', value=value))


@app.route('/order')
def order():
    return render_template('order.html', a=Order.query.filter_by().all())


@app.route('/order/<value>')
def order_by_id(value):
    return render_template('order_by_id.html', a=Order.query.get(value))


@app.route('/order/<value>/delete')
def order_delete(value):
    Order.query.filter(Order.order_id == value).delete()
    db.session.commit()
    return redirect(url_for('order'))


@app.route('/order/<value>/change')
def order_change(value):
    return render_template('order_change.html', a=Order.query.get(value))


@app.route('/order/<value>/change/success', methods=['POST'])
def order_change_success(value):
    new_order_date = request.form['order_date']
    new_time_of_order = request.form['time_of_order']
    new_waiter_id = request.form['waiter_id']
    new_order_price = request.form['order_price']
    new_service_quality_assessment = request.form['service_quality_assessment']
    Order.query.filter(Order.order_id == value).update({'order_date': new_order_date,
                                                        'time_of_order': new_time_of_order,
                                                        'order_price': new_order_price,
                                                        'service_quality_assessment': new_service_quality_assessment,
                                                        'waiter_id': new_waiter_id})
    db.session.commit()
    return redirect(url_for('order_by_id', value=value))

@app.route('/waiter')
def waiter():
    return render_template('waiter.html', a=Waiter.query.filter_by().all())


@app.route('/waiter/<value>')
def waiter_by_id(value):
    return render_template('waiter_by_id.html', a=Waiter.query.get(value))


@app.route('/waiter/<value>/delete')
def waiter_delete(value):
    Waiter.query.filter(Waiter.waiter_id == value).delete()
    db.session.commit()
    return redirect(url_for('waiter'))


@app.route('/waiter/<value>/change')
def waiter_change(value):
    return render_template('waiter_change.html', a=Waiter.query.get(value))


@app.route('/waiter/<value>/change/success', methods=['POST'])
def waiter_change_success(value):
    new_first_name = request.form['first_name']
    new_last_name = request.form['last_name']
    new_email = request.form['email']
    new_address = request.form['address']
    new_salary = request.form['salary']
    new_work_experience = request.form['work_experience']
    Waiter.query.filter(Waiter.waiter_id == value).update({'first_name': new_first_name, 'last_name': new_last_name,
                                                         'email': new_email, 'address': new_address, 'salary': new_salary,
                                                         'work_experience': new_work_experience})
    db.session.commit()
    return redirect(url_for('waiter_by_id', value=value))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/restaurant'


if __name__ == '__main__':
    app.run(debug=True)

