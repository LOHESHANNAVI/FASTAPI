import psycopg2

def get_postgres_data():

    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="password",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM test_table")

    rows = cur.fetchall()

    columns = [desc[0] for desc in cur.description]

    result = []

    for row in rows:
        result.append(dict(zip(columns, row)))

    cur.close()
    conn.close()

    return result