import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",            
        password="ashok45",        
        database="hospital_management"
    )
    print("✅ Database connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")

    for row in cursor.fetchall():
        print(row)

    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Something went wrong: {err}")

from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ashok45",
        database="hospital_management"
    )

@app.get("/doctors")
def read_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctors")
    result = cursor.fetchall()
    conn.close()
    return result

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hospital Management API working!"}
