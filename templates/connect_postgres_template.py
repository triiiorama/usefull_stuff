import psycopg2


db_host = '127.0.0.1'
db_port = '5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = '123'

connection = psycopg2.connect(host = db_host,
                              port = db_port,
                              dbname = db_name,
                              user = db_user, 
                              password = db_password)
                              
if __name__ == '__main__':
    connection = bool(connection)
    print(connection)
