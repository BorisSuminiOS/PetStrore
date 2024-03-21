import requests

from utils.http_methods import Http_methods

base_url = 'https://petstore.swagger.io/v2'

class Petstore_api():
    '''API сайта Зоомагазин'''

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


