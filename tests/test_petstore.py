import json
from utils.api_petstore import Petstore_api
from utils.checking import Checking

id_pet = 123456789
name_category = 'Семейство обезьян'
name_pet = 'King-Kong'
url_photo = 'https://img.razrisyika.ru/kart/23/90336-king-kong-3.jpg'
status = 'available'
tag_name = 'Обезьяна'
image = 'images/King-Kong.jpg'

class Test_pets():
    '''Тестирование питомцев'''

    # def test_find_pet_by_status(self):
    #     '''Тест на поиск питомца по статусу'''
    #     for i in ['available', 'pending', 'sold']:
    #         response = Petstore_api.find_pet_by_status(i)
    #         required_fields = json.loads(response.text)
    #         Checking.check_all_required_fields(response, required_fields)
    #         Checking.check_status_code(response, 200)
    #
    # def test_add_new_pet(self):
    #     '''Тест на добавление нового питомца'''
    #     response = Petstore_api.add_new_pet(id_pet, name_category,name_pet,url_photo,status,tag_name)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    # def test_search_pet_id(self):
    #     '''Тест на проверку питомца по ID'''
    #     response = Petstore_api.search_pet_id(id_pet)
    #     Checking.check_json_value(response, 'id',id_pet)
    #     Checking.check_status_code(response, 200)
    #
    # def test_uploading_pet_image(self):
    #     '''Тест на загрузку картинки питомца по id'''
    #     response = Petstore_api.uploading_pet_image(image,'jpeg', id_pet)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    def test_update_pet_data(self):
        '''Тест на обновления данных существующего питомца'''
        name_category = 'Семейство кошачьих'
        name_pet = 'Персик'
        tag_name = 'Кот'
        url_photo = 'https://www.purina.ru/sites/default/files/2021-10/amer-korotkoserst-2.jpg'
        response = Petstore_api.update_pet_data(id_pet, name_category, name_pet, url_photo, status, tag_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)




