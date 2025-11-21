from sql_connection import get_sql_connection
import mysql.connector

def get_order_detail(connection):

    query = "SELECT orders_id, customer_name, total, date_time FROM grocery_store.orders"
    #query="select * from orders"

    result = []
    
    try:
        cursor = connection.cursor() 
        cursor.execute(query)

        #result = cursor.fetchall()
        #print(result)
        
        for (order_id,customer_name,total,date_time) in cursor:
            result.append(
                 {
                      'order_id' : order_id,
                      'customer_name' : customer_name,
                      'total' : total,
                      'date_time' : date_time,
                 }
            )

    except mysql.connector.Error as err:
        print('Error from orders get : ',err)

    finally:
        if connection.is_connected():
            return result

if __name__=='__main__':
        connection = get_sql_connection()
        


