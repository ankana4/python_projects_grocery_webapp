def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


#def insert_new_uom(connection, uom):
    #cursor = connection.cursor()
    #query = f"INSERT INTO uom (uom_name) VALUES ('{uom['name']}');"
    #cursor.execute(query)
    #connection.commit()
    #return cursor.lastrowid

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))
    #print(insert_new_uom(connection, {
        #'name': 'liter'
    #}))
