# api_client.py
import allure
import requests
from config.url_config import Links

class PetStoreClient:
    API_URL = Links.BASE_URL

    def get_pet(self, pet_id):
        url = f"{self.API_URL}/pet/{pet_id}"
        headers = {'accept': 'application/json'}
        with allure.step(f'GET request to: {url}'):
            return requests.get(url, headers=headers)

    def post_pet(self, pet_data):
        url = f"{self.API_URL}/pet"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        with allure.step(f'POST request to: {url}'):
            return requests.post(url, headers=headers, json=pet_data)

    def put_pet(self, pet_data):
        url = f"{self.API_URL}/pet"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        with allure.step(f'PUT request to: {url}'):
            return requests.put(url, headers=headers, json=pet_data)

    def delete_pet(self, pet_id):
        url = f"{self.API_URL}/pet/{pet_id}"
        headers = {'accept': 'application/json'}
        with allure.step(f'DELETE request to: {url}'):
         return requests.delete(url, headers=headers)