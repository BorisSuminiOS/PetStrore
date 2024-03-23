import requests
import datetime
import random
from utils.http_methods import Http_methods
from utils.logger import Logger

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type':'application/json'}

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
        Logger.add_request(url_post,"POST")
        result_post = requests.post(url_post, data=data, files=files)
        Logger.add_response(result_post)
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
        Logger.add_request(url_post, "POST")
        result_post = requests.post(url_post, data=data)
        Logger.add_response(result_post)
        print(result_post.text)
        return result_post

    @staticmethod
    def delete_pet(id_pet):
        '''Удаление питомца из магазина'''
        url_delete = f'{base_url}/pet/{id_pet}'
        headers = {
            'api_key' : 'special-key'
        }
        Logger.add_request(url_delete, "DELETE")
        result_delete = requests.delete(url_delete, headers=headers)
        Logger.add_response(result_delete)
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
        Logger.add_request(url_delete, "DELETE")
        result_delete = requests.delete(url_delete)
        Logger.add_response(result_delete)
        print(result_delete.text)
        return result_delete

class User():
    '''Операции над пользователем '''

    @staticmethod
    def create_user(user_name, first_name, last_name, email, password, phone):
        '''Регистрация нового пользователя'''
        body_json = {
                    "id": random.randint(1, 100),
                    "username": user_name,
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "password": password,
                    "phone": phone,
                    "userStatus": random.randint(1, 100)
                    }
        url_post = f'{base_url}/user'
        result_post = Http_methods.post(url_post, body_json)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_user_by_name(user_name):
        '''Поиск пользователя по имени'''
        url_get = f'{base_url}/user/{user_name}'
        result_get = Http_methods.get(url_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def create_lst_user():
        '''Создание новых пользователей'''
        body_json = [
                {
                "id": random.randint(1, 100),
                "username": 'QaMark',
                "firstName": 'Mark',
                "lastName": "Moss",
                "email": 'Mark@mail.ru',
                "password": '123123',
                "phone": '1234123123',
                 "userStatus": random.randint(1, 100)
                },
            {
                "id": random.randint(1, 100),
                "username": 'Qa_wer',
                "firstName": 'Wer',
                "lastName": "Mosswer",
                "email": 'WER@mail.ru',
                "password": '12asd312asdeg3',
                "phone": '123412312323123',
                "userStatus": random.randint(1, 100)
            }
        ]
        url_post = f'{base_url}/user/createWithArray'
        result_post = Http_methods.post(url_post, body_json)
        print(result_post.text)
        return result_post

    @staticmethod
    def update_user_by_user_name(user_name):
        '''Изменение данных существующего пользователя по User name'''
        body_json = {
            "id": random.randint(1, 100),
            "username": user_name,
            "firstName": 'Alex',
            "lastName": 'Sumin',
            "email": 'AlexAlex@mail.ru',
            "password": 'qwerty123123123',
            "phone": '898876653123',
            "userStatus": random.randint(1, 100)
        }
        url_put = f'{base_url}/user/{user_name}'
        result_put = Http_methods.put(url_put, body_json)
        print(result_put.text)
        return result_put

    @staticmethod
    def login(user_name,password):
        '''Авторизация пользователя в системе'''
        url_get = f'{base_url}/user/login?{user_name}&{password}'
        result_get = Http_methods.get(url_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def logout():
        '''Выход пользователя из текущего сеанса'''
        url_get = f'{base_url}/user/logout'
        result_get = Http_methods.get(url_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def delete_user(user_name):
        '''Удалить пользователя'''
        url_delete = f'{base_url}/user/{user_name}'
        Logger.add_request(url_delete, "DELETE")
        result_delete = requests.delete(url_delete)
        Logger.add_response(result_delete)
        print(result_delete.text)
        return result_delete


