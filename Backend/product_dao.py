from sql_connection import get_sql_connection
import mysql.connector


def get_all_products(connection):
     
    query="select products.Product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id;"
    
    #insert data to db
    #query1="INSERT INTO grocery_store.products (Product_id, name, uom_id, price_per_unit) VALUES (%s, %s, %s, %s)"
    #values = (3, "banana", 2, 40) 

    try:
        cursor = connection.cursor()
        #cursor.execute(query1,values) #insert data to db
        cursor.execute(query)
        #connection.commit() #for insert to db

        # Fetch results
        """results = cursor.fetchall()

        for row in results:
            print(row)"""
        
        response = []
        
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
        print('Error :',err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
            return response

if __name__=='__main__':
        connection = get_sql_connection()
        print(get_all_products(connection))