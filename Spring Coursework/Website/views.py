from flask import Blueprint, render_template, request, flash, session, url_for, redirect
from .models import Item
from .shop_items import get_products


#Stores all the paths that a user can access
views = Blueprint('views', __name__)

#Whenever this URL is accessed, the function below will run, i.e. the first one returns the home page
@views.route('/')
def home():
    return render_template("carousel.html", products=get_products(""))

@views.route('/account')
def account():
    return render_template("account.html")


#Product Pages
@views.route('/product/1')
def get_countdown():
    return render_template("product_pages/countdown.html", item=get_products('1')) 
@views.route('/product/2')
def get_forgetful():
    return render_template("product_pages/forgetful.html", item=get_products('2'))
@views.route('/product/3')
def get_madness():
    return render_template("product_pages/madness.html", item=get_products('3'))
@views.route('/product/4')
def get_timeTravel():
    return render_template("product_pages/timeTravel.html", item=get_products('4'))

#BASKET STUFF    
@views.route('/add_to_basket/<int:product_id>', methods=['POST', 'GET'])
def add_to_basket(product_id):
    product = Item.query.get(product_id) #Gets the item from models.py based on its id

    basket = session.get('basket', [])

    #Checks if a product is already in the basket
    for basket_item in basket:
        if basket_item['id'] == product.id:
            basket_item['quantity'] += 1
            session['basket'] = basket
            flash(f'Added {product.name} to basket')
            return redirect(url_for('views.view_basket'))
        
    #Else adds the product to the basket and creates a session for it
    basket.append(dict(id=product.id, name=product.name, price=product.price, image=product.image, quantity=1))
    session['basket'] = basket

    return redirect(url_for('views.view_basket'))

@views.route('/basket', methods=['GET', 'POST'])
def view_basket():
    totalPrice = 0 #Gets calculated at the end
    basket = session.get('basket', []) #Gets the current basket session
    product_ids = [product['id'] for product in basket] #Gets all the product ids from the basket
    products = Item.query.filter(Item.id.in_(product_ids)).all() #Gets the names of all the products from their ids
    totalPrice = sum(product['price'] * product['quantity'] for product in basket) #Calculates the sum of the items X the price

    #Finds the quantity of each item in the basket
    for product in products:
        for basket_item in basket:
            if basket_item['id'] == product.id:
                product.quantity = basket_item['quantity']
                break
    
    return render_template('basket.html', products=products, basket=basket, totalPrice=totalPrice)

@views.route('/empty_basket')
def empty_basket():
    session.pop('basket', None)
    return redirect(url_for('views.home'))

@views.route('/remove_from_basket/<int:product_id>', methods=['POST', 'GET'])
def remove_from_basket(product_id):
    basket = session.get('basket', [])
    for product in basket:
        if product['id'] == product_id: #Checks if there are more than 1 product in a basket
            if product['quantity'] > 1:
                product['quantity'] -= 1
                session['basket'] = basket
            else:
                basket.remove(product)
                session['basket'] = basket
            break

    return redirect(url_for('views.view_basket'))


@views.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        email = request.form.get('email')
        cardNum = request.form.get('card-number')
        cvc = request.form.get('cvc-num')

        if len(cardNum) != 16:
            flash('Card Number must be 16 digits', category='error')
        if cardNum.isnumeric == False:
            flash('Card Number must contain numbers', category='error')
        if len(cvc) != 3:
            flash('CVC number must be 3 digits', category='error')
        if cardNum.isnumeric == False:
            flash('CVC must contain numbers', category='error')
        else:
            flash('Payment succesful!', category='success')
            return redirect(url_for('views.empty_basket'))
    
    return render_template("payment.html")
