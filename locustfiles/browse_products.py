from locust import HttpUser, task, between
from random import choice

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    # Define collection and product IDs
    collection_ids = [1, 2, 3, 4]
    product_ids = [1, 2, 3, 4]

    @task(2)
    def view_products(self):
        print('Viewing products')
        collection_id = choice(self.collection_ids)
        self.client.get(
            f'/store/products/?collection_id={collection_id}', 
            name='/store/products'
        )

    @task(4)
    def view_product(self):
        print('Viewing product details')  
        product_id = choice(self.product_ids)
        self.client.get(
            f'/store/products/{product_id}',
            name='/store/products/:id'
        )

    @task(1)
    def add_to_cart(self):
        print('Adding product to cart')  
        product_id = choice(self.product_ids)  
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            json={'product_id': product_id, 'quantity': 1}
        )

    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']
