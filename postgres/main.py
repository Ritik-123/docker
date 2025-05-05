import psycopg2

# Database connection config
DB_NAME = "user"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "postgres"
DB_PORT = "5432"

# Connect to PostgreSQL
def connect():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER,
            password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        print("Connected to the database.")
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Create table
def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        conn.commit()
        print("Table created.")

# Insert data
def insert_user(conn, name, email):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
        conn.commit()
        print(f"User {name} added.")

# Read data
def get_users(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        for row in rows:
            print(row)

# Update user
def update_user_email(conn, user_id, new_email):
    with conn.cursor() as cur:
        cur.execute("UPDATE users SET email = %s WHERE id = %s;", (new_email, user_id))
        conn.commit()
        print("User email updated.")

# Delete user
def delete_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()
        print("User deleted.")

# Main
if __name__ == "__main__":
    conn = connect()
    if conn:
        create_table(conn)
        insert_user(conn, "Alice", "alice@example.com")
        insert_user(conn, "Bob", "bob@example.com")
        print("All users:")
        get_users(conn)
        update_user_email(conn, 1, "alice@newmail.com")
        delete_user(conn, 2)
        print("Final user list:")
        get_users(conn)
        conn.close()
