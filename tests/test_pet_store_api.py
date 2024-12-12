# test_pet_store_api.py
import allure

from config.api_client import PetStoreClient

@allure.feature("API Functionality")
class TestPetStoreApi:
    client = PetStoreClient()

    @allure.title("Set Pet data")
    def test_post_pet(self):
        # Формируем данные для нового питомца
        new_pet_data = {
            "id": 13,
            "category": {
                "id": 1,
                "name": "dog"
            },
            "name": "Stiven",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "black"
                }
            ],
            "status": "available"
        }
        # Отправляем POST запрос
        response = self.client.post_pet(new_pet_data)
        with allure.step("Проверяем, что статус-код ответа 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Проверяем содержание ответа"):
            pet = response.json()
            assert pet is not None
            assert pet['name'] == new_pet_data['name']  # Проверяем, что имя питомца соответствует

    @allure.title("Get Pet data")
    def test_get_pet(self):
        response = self.client.get_pet(13)
        with allure.step("Проверяем, что статус-код ответа 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step(" Проверяем, что возвращаемые данные имеют нужный формат (JSON)"):
            assert response.headers['Content-Type'] == 'application/json'
        with allure.step("Проверяем содержание ответа"):
            pet = response.json()
            assert pet is not None
        with allure.step("Проверяем, что id питомца соответствует запросу"):
            assert pet['id'] == 13  # Проверяем, что id питомца соответствует запросу

    @allure.title("Change Pet data")
    def test_put_pet(self):
        # Формируем данные для нового питомца
        new_pet_data = {
            "id": 13,
            "category": {
                "id": 2,
                "name": "big_dog"
            },
            "name": "Gomer",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "brown"
                }
            ],
            "status": "unavailable"
        }
        # Отправляем PUT запрос
        response = self.client.post_pet(new_pet_data)
        with allure.step("Проверяем, что статус-код ответа 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Проверяем содержание ответа"):
            pet = response.json()
            assert pet is not None
        with allure.step("Проверяем, что имя питомца соответствует"):
            assert pet['name'] == new_pet_data['name'], f"Ожидалось имя '{new_pet_data['name']}', получено '{pet['name']}'"

    @allure.title("Delete Pet data")
    def test_delete_pet(self):
        response = self.client.delete_pet(13)
        with allure.step("Проверяем, что статус-код ответа 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        # Проверяем, что возвращаемые данные имеют нужный формат (например, JSON)
        assert response.headers['Content-Type'] == 'application/json'
        with allure.step("Проверяем содержание ответа"):
            pet = response.json()
            assert pet is not None

if __name__ == '__main__':
    import pytest
    pytest.main()