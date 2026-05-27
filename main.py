from fastapi import FastAPI
import psycopg2

app = FastAPI()

# conexão com postgres
conn = psycopg2.connect(
    host="db",
    database="devopsdb",
    user="admin",
    password="admin"
)

cursor = conn.cursor()

# cria tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    status VARCHAR(50)
)
""")

conn.commit()

@app.get("/")
def home():
    return {"message": "API DevOps rodando 🚀"}

@app.post("/tasks")
def create_task(task: dict):

    cursor.execute(
        "INSERT INTO tasks (titulo, status) VALUES (%s, %s)",
        (task["titulo"], task["status"])
    )

    conn.commit()

    return {"message": "Tarefa criada"}

@app.get("/tasks")
def list_tasks():

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    return tasks