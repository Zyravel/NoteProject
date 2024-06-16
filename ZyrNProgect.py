import requests
import pprint

user_cart = 'https://fakestoreapi.com/users'
sp_user_cart = []
response = requests.get(user_cart).json()
pprint.pprint(response)