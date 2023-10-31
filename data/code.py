import psycopg2
import json
# import datetime
# path_to_file = 'data/newdata.json'
# with open(path_to_file, 'r') as data_file:
#     data = json.load(data_file)

# collection_array = []
# for item in data:
#     collection_array.append(json.dumps(item))

try:
    conn = psycopg2.connect(database="database_development", user="testing", password="testing", host="127.0.0.1", port="5432")
    print("Opened database successfully")
    cur = conn.cursor()

    # retrieve data from table row by row and print each row of data from postgres
    # query = "SELECT * FROM \"Data\""
    # cur.execute(query)
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)

    # cur.execute("""SELECT table_name FROM information_schema.tables
    #     WHERE table_schema = 'public'""")

    # for table in cur.fetchall():
    #      print(table)

    #delete row from table

    query = "Delete from \"Location\" where name='tirpathi foods'"
    cur.execute(query)
    
    # query = "DELETE FROM \"Data\""
    # cur.execute(query)


    # for element in collection_array:
    #     element=json.loads(element)
    #     query = "INSERT INTO \"Data\" (name, type, description, state, mapslink, region, createdAt) VALUES (%s, %s, %s, %s, %s, %s)"
    #     values = (element['name'], element['type'], element['description'], element['state'], " " , element['region'])
    #     cur.execute(query, values)

        # create a query to insert data into table name users with column name and email
        # query = "INSERT INTO \"Data\" (name,type,description,state,mapslink,region) VALUES ('"+element['name']+"','"+element['type']+"','"+element['description']+"','"+element['state']+"','"+element['mapsLink']+"','"+element['region']+"')"
        # query = "INSERT INTO \"Data\" (name,type,description,state,region) VALUES ('"+element['name']+"','"+element['type']+"','"+element['description']+"','"+element['state']+"','"+element['region']+"')"
        # cur.execute(query)

    print("Successfully inserted records")

except psycopg2.Error as e:
    print("Error:", e)
    raise

finally:
    conn.commit()
    conn.close()
    print("Connection is closed")
