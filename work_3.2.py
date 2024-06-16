import requests


url_cart = 'https://fakestoreapi.com/carts/user/'
url_product = 'https://fakestoreapi.com/products/'
url_user = 'https://fakestoreapi.com/users/'
url_users = 'https://fakestoreapi.com/user'

response_users = requests.get(url_user).json() 

x_user = input('Введите username пользователя или его ID: ')
id_x_user = x_user
if not x_user.isdigit():
    for user in response_users:
        if user['username'] == x_user:
            id_x_user = str(user['id'])

response_cart = requests.get(url_cart + id_x_user).json()

sp_products = dict()
for prod in response_cart:
    for cart in prod['products']:
        if sp_products.get(cart['productId']):
            sp_products[cart['productId']] = sp_products[cart['productId']] + cart['quantity']
        else:
            sp_products[cart['productId']] = cart['quantity']

for key, value in sp_products.items():
    resp = requests.get(url_product + str(key)).json()
    print(f' Куплено {resp['title']} {value} штук')
