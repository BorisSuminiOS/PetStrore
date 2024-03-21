from utils.http_methods import Http_methods


base_url = 'https://petstore.swagger.io/v2'

class Petstore_api():
    '''API сайта Зоомагазин'''

    @staticmethod
    def find_pet_by_status(status):
        '''Найти питомцев по статусу (available, pending, sold)'''
        resource_get = '/pet/findByStatus'
        params = '?status='
        url_get = f'{base_url}{resource_get}{params}{status}'
        result_get = Http_methods.get(url_get)
        print(f'ПИТОМЦЫ: {result_get.text}\nСТАТУС ПИТОМЦЕВ: {status}')
        return result_get
    @staticmethod
    def add_new_pet(id_pet, name):
        '''Добавить нового питомца'''
        body_json = {"id": id_pet,"category": {"id": 0,"name": "string"},
                        "name": name,
                        "photoUrls": ["string"],
                        "tags": [{"id": 0,"name": "string"}],
                        "status": "available"}
        resource_post = '/pet'
        url_post = base_url + resource_post
        result_post = Http_methods.post(url_post, body_json)
        print(f'ОТВЕТ ОТ СЕРВЕРА: {result_post.text}')
        return result_post

