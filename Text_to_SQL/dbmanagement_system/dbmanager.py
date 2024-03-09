from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="A2ZDigital"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT * FROM DBManager WHERE UserId = %s AND UserPassword = %s", (username, password))
    user = cursor.fetchone()
    if user:
        return redirect(url_for('main'))
    else:
        return "Invalid username or password"

@app.route('/get_categories')
def get_categories():
    cursor.execute("SELECT Categoryid, Category FROM Category")
    categories = cursor.fetchall()
    categories_data = [{'Categoryid': category[0], 'Category': category[1]} for category in categories]
    return jsonify(categories_data)

@app.route('/get_items')
def get_items():
    category_id = request.args.get('category_id')
    cursor.execute("SELECT Itemid FROM Items WHERE Categoryid = %s", (category_id,))
    items = cursor.fetchall()
    return jsonify(items)

@app.route('/get_item_details')
def get_item_details():
    category_id = request.args.get('category_id')
    item_id = request.args.get('item_id')

    cursor.execute("SELECT Brand, ModelName, Specifications FROM Items WHERE Categoryid = %s AND Itemid = %s",
                   (category_id, item_id))
    item_details = cursor.fetchone()

    return jsonify({
        'brand_name': item_details[0],
        'model_name': item_details[1],
        'specifications': item_details[2]
    })

@app.route('/update_stock', methods=['POST'])
def update_stock():
    if request.method == 'POST':
        item_id = request.form['item']
        number_of_items = request.form['number_of_items']

        try:
            cursor.execute("UPDATE Stock SET Quantity = Quantity + %s WHERE Itemid = %s", (number_of_items, item_id))
            db.commit()
            return redirect(url_for('stock_update'))  # Redirect to the stock update page
        except Exception as e:
            db.rollback()
            return "Error updating stock: " + str(e)

@app.route('/update_sales', methods=['POST'])
def update_sales():
    if request.method == 'POST':
        item_id = request.form['item']
        number_of_items = request.form['number_of_items']

        try:
            cursor.execute("UPDATE Sales SET QuantitySold = QuantitySold + %s WHERE Itemid = %s",
                           (number_of_items, item_id))
            cursor.execute("UPDATE Stock SET Quantity = Quantity - %s WHERE Itemid = %s",
                           (number_of_items, item_id))
            db.commit()

            return redirect(url_for('sales_update'))
        except Exception as e:
            db.rollback()
            return "Error updating sales and stock: " + str(e)

@app.route('/update_discount', methods=['POST'])
def update_discount():
    if request.method == 'POST':
        item_id = request.form['item']
        discount = request.form['discount']

        try:
            cursor.execute("UPDATE Discount SET Discount = %s WHERE Itemid = %s", (discount, item_id))
            db.commit()
            return redirect(url_for('discount_update'))
        except Exception as e:
            db.rollback()
            return "Error updating sales and stock: " + str(e)


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        item_id = request.form['item']
        category_id = request.form['category']
        brand = request.form['brand_name']
        model_name = request.form['model_name']
        specifications = request.form['specifications']
        price = request.form['price']

        try:
            cursor.execute("INSERT INTO Items (Itemid, Categoryid, Brand, ModelName, Specifications, Price) VALUES (%s, %s, %s, %s, %s, %s)",
                           (item_id, category_id, brand, model_name, specifications, price))
            db.commit()

            return jsonify({'message': 'Product added successfully'}), 200
        except Exception as e:
            db.rollback()
            return jsonify({'error': 'Failed to add product', 'details': str(e)}), 500

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/stock_update')
def stock_update():
    return render_template('stock_update.html')

@app.route('/sales_update')
def sales_update():
    return render_template('sales_update.html')

@app.route('/new_product')
def new_product():
    return render_template('new_product.html')

@app.route('/discount_update')
def discount_update():
    return render_template('discount_update.html')

if __name__ == '__main__':
    app.run(debug=True)

