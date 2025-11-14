import mysql.connector

query="SELECT * FROM grocery_store.products"

"""query1="INSERT INTO grocery_store.products (Product_id, name, uom_id, price_per_unit) VALUES (%s, %s, %s, %s)"
values = (3, "banana", 2, 40)""" #insert data to db

try:
    connection = mysql.connector.connect(host='localhost', database='grocery_store', user='root',password='root')
    cursor = connection.cursor()
    """cursor.execute(query1,values)""" #insert data to db
    cursor.execute(query)
    """connection.commit()""" #for insert to db

    # Fetch results
    """results = cursor.fetchall()

    for row in results:
        print(row)"""
    
    for (Product_id,name,uom_id,price_per_unit) in cursor:
        print(Product_id,name,uom_id,price_per_unit)
        
except mysql.connector.Error as err:
    print('Error :',err)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")