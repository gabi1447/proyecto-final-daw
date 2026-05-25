import requests
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
from datetime import datetime

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
        self.cur = self.conn.cursor()

class Cronjob:
    products_to_retrieve = [
        {
            "product": "gameboy advance",
            "db_table_name": "gameboy"
        }
    ]
    
    def __init__(self, dbconnection: DbConnection):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token_url = os.getenv("TOKEN_URL")
        self.api_url = os.getenv("API_URL")
        self._token = None
        self.db = dbconnection
    
    @property
    def token(self):
        if self._token is None:
            payload = {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope"
            }
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            
            response = requests.post(self.token_url, 
                                    auth=(self.client_id, self.client_secret), 
                                    data=payload, 
                                    headers=headers)
            self._token = response.json()['access_token']
            return self._token
        else:
            return self._token
    
    @staticmethod
    def log_info():
        with open('/var/log/cron.log', 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            f.write(f'Products were restored at {timestamp}\n')

    def get_product_data(self, product):
        url_params = {'q': product, 'limit': 5}
        headers = {
            'Authorization': f'Bearer {self.token}',
        }
        response = requests.get(self.api_url, params=url_params, headers=headers)
        return response.json()
    
    def wipe_product_data(self):
        sql = "TRUNCATE TABLE products RESTART IDENTITY"
        self.db.cur.execute(sql)
        self.db.conn.commit()
        
    def insert_products(self):
        sql = """
            INSERT INTO products (name, price, currency, image_url, item_link, category_id)
            VALUES %s;
        """
        execute_values(
            self.db.cur,
            sql,
            self.filter_product_data('gameboy', 1)
        )
        self.db.conn.commit()
    
    def filter_product_data(self, product_to_get, category_id):
        products = self.get_product_data(product_to_get)['itemSummaries']
        products_to_store = []
        for product in products:
            product_data = (
                 product['title'],
                 float(product['price']['value']),
                 product['price']['currency'],
                 product['image']['imageUrl'],
                 product['itemWebUrl'],
                 category_id
            )
            products_to_store.append(product_data)
        return products_to_store
        
def main():
    cron_job = Cronjob(DbConnection())
    cron_job.wipe_product_data()
    cron_job.insert_products()
    cron_job.log_info()
main()