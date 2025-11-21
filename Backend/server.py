from flask import Flask, jsonify
import product_dao
import orders
from sql_connection import get_sql_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

connection = get_sql_connection()

@app.route("/getProduct", methods=['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response
    
@app.route("/deleteProduct", methods=['POST'])
def delete_products():
    return_id = product_dao.delete_products(connection, request.form[product_id])
    response = jsonify({'product_id' : return_id})
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

@app.route("/getAllOrders", methods=['GET'])
def get_orders():
    order = orders.get_order_detail(connection)
    response = jsonify(order)
    response.headers.add("Access-Control-Allow-Origin", '*')
    return response

if __name__ == "__main__":
    print("Flask server for Gs")
    app.run(port=5000)