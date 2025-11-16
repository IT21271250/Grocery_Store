from flask import Flask, jsonify
import product_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route("/getProduct", methods=['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response
    

if __name__ == "__main__":
    print("Flask server for Gs")
    app.run(port=5000)