from sql_connection import get_sql_connection
import mysql.connector

#Read all products
def get_all_products(connection):
     
    query="select products.Product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id;"

    response = []

    try:
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch results
        """results = cursor.fetchall()

        for row in results:
            print(row)"""
        
        for (Product_id,name,uom_id,price_per_unit, uom_name) in cursor:
            response.append(
                 {
                      'Product_id' : Product_id,
                      'name' : name,
                      'uom_id' : uom_id,
                      'price_per_unit' : price_per_unit,
                      'uom_name' : uom_name
                 }
            )
            
    except mysql.connector.Error as err:
        print('Error from get : ',err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
            return response

#insert new products
def insert_new_product(connection, product):
     
    #insert data to db
    query="INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    values = (product['product_name'], product['uom_id'], product['price_per_unit']) 
    #values = ('Towel','1','1000')

    try:
        cursor = connection.cursor()
        cursor.execute(query, values) #insert data to db
        connection.commit() #for insert to db

        return cursor.lastrowid #get the last row id

    except mysql.connector.Error as err:
        print('Error from insert :',err)


#Delete new products
def delete_product(connection, product_id):
     
    #insert data to db
    query= ("DELETE FROM products where product_id = " + str(product_id))

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except mysql.connector.Error as err:
        print('Error from Delete :',err)

if __name__=='__main__':
        connection = get_sql_connection()
        print(get_all_products(connection))
        #print(delete_product(connection,11))
        #print(insert_new_product(connection))