import requests
import datetime
from utils.http_methods import Http_methods

base_url = 'https://petstore.swagger.io/v2'

class Pets_api():
    '''API методы, create, read, update, delete pets (CRUD)'''

    @staticmethod
    def find_pet_by_status(status):
        '''Найти питомцев по статусу (available, pending, sold)'''
        resource_get = '/pet/findByStatus'
        params = f'?status={status}'
        url_get = f'{base_url}{resource_get}{params}'
        result_get = Http_methods.get(url_get)
        print(f'Питомцы: {result_get.text}\nСтатус питомцев: {status}')
        return result_get

    @staticmethod
    def add_new_pet(id_pet, category_name, name_pet,url_photo,status,tag_name):
        '''Добавить нового питомца'''
        body_json = {"id": id_pet,"category": {"id": id_pet,"name": category_name},
                        "name": name_pet,
                        "photoUrls": [url_photo],
                        "tags": [{"id": id_pet,"name": tag_name}],
                        "status": status}
        resource_post = '/pet'
        url_post = base_url + resource_post
        result_post = Http_methods.post(url_post, body_json)
        print(f'Ответ от сервера: {result_post.text}')
        return result_post

    @staticmethod
    def search_pet_id(id_pet):
        '''Поиск питомца по ID'''
        resource_get = f'/pet/{id_pet}'
        url_get = base_url + resource_get
        result_get = Http_methods.get(url_get)
        print(f'Ответ от сервера: {result_get.text}')
        return result_get

    @staticmethod
    def uploading_pet_image(image, format_image, id_pet):
        '''Загрузка картинки питомца по id'''
        data = {'additionalMetadata': format_image}
        files = {'file': ('image', open(f'{image}', 'rb'),'image/jpeg')}
        url_post = f'{base_url}/pet/{id_pet}/uploadImage'
        result_post = requests.post(url_post, data=data, files=files)
        print(result_post.text)
        return result_post

    @staticmethod
    def update_pet_data(id_pet, category_name, name_pet,url_photo,status,tag_name):
        '''Обновления данных существующего питомца'''
        body_json = {"id": id_pet,"category": {"id": id_pet,"name": category_name},
                        "name": name_pet,
                        "photoUrls": [url_photo],
                        "tags": [{"id": id_pet,"name": tag_name}],
                        "status": status}
        resource_put = '/pet'
        url_put = base_url + resource_put
        result_put = Http_methods.put(url_put, body_json)
        print(f'Ответ от сервера: {result_put.text}')
        return result_put

    @staticmethod
    def updating_pet_with_form_data(id_pet, name_pet, status):
        '''Обновления данных питомца с помощью form-data'''
        data = {'name' : name_pet, 'status' : status}
        url_post = f'{base_url}/pet/{id_pet}'
        result_post = requests.post(url_post, data=data)
        print(result_post.text)
        return result_post

    @staticmethod
    def delete_pet(id_pet):
        '''Удаление питомца из магазина'''
        url_delete = f'{base_url}/pet/{id_pet}'
        headers = {
            'api_key' : 'special-key'
        }
        result_delete = requests.delete(url_delete, headers=headers)
        print(result_delete.text)
        return result_delete

class Petstore_api():
    '''Доступ к заказам зоомагазина'''

    @staticmethod
    def place_order_pet(id_pet, count_pet, status,order_number):
        '''Оформление заказа на питомца'''
        body_post = {
                    "id": order_number,
                    "petId": id_pet,
                    "quantity": count_pet,
                    "shipDate": str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')),
                    "status": status,
                    "complete": True
                    }
        url_post = f'{base_url}/store/order'
        result_post = Http_methods.post(url_post, body_post)
        print(result_post.text)
        return result_post

    @staticmethod
    def search_order_number(order_number):
        '''Поиск заказа по номеру заказа'''
        url_get = f'{base_url}/store/order/{order_number}'
        result_get = Http_methods.get(url_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def delete_by_order_number(order_number):
        '''Удаление заказа по номеру заказа'''
        url_delete = f'{base_url}/store/order/{order_number}'
        result_delete = requests.delete(url_delete)
        print(result_delete.text)
        return result_delete

