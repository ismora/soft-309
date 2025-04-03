from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Configuración desde variables de entorno
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "test_db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

@app.route("/")
def hello():
    return "¡Entorno efímero funcionando!"

@app.route("/check-db")
def check_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return "Conexión a DB exitosa"
    except Exception as e:
        return f"Error de conexión: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)