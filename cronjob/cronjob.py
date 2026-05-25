import requests
import psycopg2
import os
from dotenv import load_dotenv

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

    def get_product_data(self, product):
        url_params = {'q': product, 'limit': 5}
        headers = {
            'Authorization': f'Bearer {self.token}',
        }
        response = requests.get(self.api_url, params=url_params, headers=headers)
        return response.json()
    
    def insert(self):
        self.db.cur.execute("INSERT INTO category (category_name) VALUES('Wii')")
        self.db.conn.commit()
    
cron_job = Cronjob(DbConnection())
cron_job.insert()