# Proyecto Final 1ºDAW

# Table of contents
1. [Data source and functionality](#data-source)
2. [Virtual machines](#virtual-machines)
3. [Architecture diagram](#architecture-diagram)

## Data source and functionality<a name="data-source"></a>
We have chosen the Ebay API as our primary 
data source of information. We will use this API to retrieve
information related to products based in our interests.

Our plan is to use a lightweight Python Backend Framework, such as
Flask or FastApi and the library requests. 

We will use FastApi/Flask to declare endpoints that we will call from the Frontend to populate the database
and additionally generate an html page with the products information consolidated in the database.

The library requests will be used directly from the backend to retrieve the information related
to the selected products. We will then parse the JSON response and insert product info in the database.

Since we have decided to use an API to retrieve product data, we will be using the **requests** library in Python
for this purpose. At first we'll need to know how the API we want to hit is built (endpoints we can attack). If the 
API is public this is usually documented in detail.

Once we know at a high level the endpoints we need to attack and the http methods that will be used per endpoint (in this
case we'll be using the GET http method primarily since our main goal is to retrieve data, not to populate any) we can 
use the requests library to perform this actions.

A very basic example from the [docs](https://requests.readthedocs.io/en/latest/) to retrieve data from 
an API would be this:

```python
import requests
url = 'https://api.github.com/user'
# We will be using the .get method since we are just retrieving information
r = requests.get(url)
# We most probably will be dealing with JSON responses from the API
# so we'll need to decode the JSON somehow to work with the data we have retrieved.
# For that will be using the .json() method to work with the data sent from the API.
r.json()
```

The moment we have parsed the data recovered from the API we can make a connection with 
the Postgres database with the library **psycopg2** and make insertions with the data we have recovered
from the API.

To configure a secure HTTPS server, we will first install nginx  because it uses little memory and is an open-source web server. Then, we install cerbot being an automatic and free toll to enable HTTPS on websites using SSL/TLS certificates with the following command:

```python
sudo cerbot --nginx
```

For two-factor authentication, we will use Google Authenticator with the googleauth library in Python.

## Virtual machines<a name="virtual-machines"></a>
For this project, two VMs will be created: one will be the server (using nginx) and the other will host the PostgreSQL database. Each has the following requirements:
- VM BBDD Postgres:
    - 4 GB RAM
    - 50 GB Virtual disk
    - Bridge adapter
    - 10.109.99.46
    - User: postgres
- VM Servidor:
    - 4 GB RAM
    - 50 GB Virtual disk
    - Bridge adapter
    - 10.109.99.184
    - User: nginx

## Architecture diagram<a name="architecture-diagram"></a>

![diagram](./img/architecture-diagram.png)