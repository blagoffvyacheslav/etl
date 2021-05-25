import psycopg2


def dump_db_to_csv(conn_string, tables):
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        for table in tables:
            query = f"COPY {table} TO STDOUT WITH DELIMITER ',' CSV HEADER;"
            with open(f'./tables/{table}.csv', 'w') as csv_file:
                cursor.copy_expert(query, csv_file)


def load_in_db_from_csv(conn_string, tables):
    with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
        for table in tables:
            query = f"COPY {table} from STDIN WITH DELIMITER ',' CSV HEADER;"
            with open(f'./tables/{table}.csv', 'r') as csv_file:
                cursor.copy_expert(query, csv_file)


db1 = "host='localhost' port=54320 dbname='db1' user='root' password='postgres'"
db2 = "host='localhost' port=5433 dbname='db2' user='root' password='postgres'"
tables = ['customer','lineitem','nation','orders','part','partsupp','region','supplier']

dump_db_to_csv(db1, tables)
load_in_db_from_csv(db2, tables)