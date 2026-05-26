from fastapi import FastAPI, Query
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class DbConnection:
    def __init__(self):
        load_dotenv()
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.db = os.getenv("POSTGRES_DB")
        self.conn = psycopg2.connect(
            host="postgres",
            port="5432",
            dbname=self.db,
            user=self.user,
            password=self.password)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        

app = FastAPI()
db = DbConnection()
    
@app.get("/api")
async def test():
    return {"message": "Hello World"}

@app.get("/api/products")
async def test_products():
    return [
        {"name": "gameboy", "price": 200},
        {"name": "PS1", "price": 150}
    ]

@app.get("/api/products/{category_id}")
async def products(
    category_id: int,
    page: int = Query(default=1, ge=1),
    size: int = Query(default=10, ge=1, le=100),
):
    offset = (page - 1) * size
    
    sql = """
        SELECT name, price, currency, image_url, item_link
        FROM products
        WHERE category_id = %s
        ORDER BY id
        LIMIT %s OFFSET %s
    """
    db.cur.execute(sql, (category_id, size, offset))
    
    rows = db.cur.fetchall()
    return rows