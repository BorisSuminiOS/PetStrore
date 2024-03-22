import json
from utils.api_petstore import Pets_api, Petstore_api, User
from utils.checking import Checking


class Test_pets():
    '''Тестирование питомцев'''

    # id_pet = 123456789
    # name_category = 'Семейство обезьян'
    # name_pet = 'King-Kong'
    # url_photo = 'https://img.razrisyika.ru/kart/23/90336-king-kong-3.jpg'
    # status = 'available'
    # tag_name = 'Обезьяна'
    # image = 'images/King-Kong.jpg'
    #
    # def test_find_pet_by_status(self):
    #     '''Тест на поиск питомца по статусу'''
    #     for i in ['available', 'pending', 'sold']:
    #         response = Pets_api.find_pet_by_status(i)
    #         required_fields = json.loads(response.text)
    #         Checking.check_all_required_fields(response, required_fields)
    #         Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_add_new_pet(cls):
    #     '''Тест на добавление нового питомца'''
    #     response = Pets_api.add_new_pet(cls.id_pet, cls.name_category,cls.name_pet,cls.url_photo,cls.status,cls.tag_name)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_search_pet_id(cls):
    #     '''Тест на проверку питомца по ID'''
    #     response = Pets_api.search_pet_id(cls.id_pet)
    #     Checking.check_json_value(response, 'id',cls.id_pet)
    #     Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_uploading_pet_image(cls):
    #     '''Тест на загрузку картинки питомца по id'''
    #     response = Pets_api.uploading_pet_image(cls.image,'jpeg', cls.id_pet)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_update_pet_data(cls):
    #     '''Тест на обновления данных существующего питомца'''
    #     name_category = 'Семейство кошачьих'
    #     name_pet = 'Персик'
    #     tag_name = 'Кот'
    #     url_photo = 'https://www.purina.ru/sites/default/files/2021-10/amer-korotkoserst-2.jpg'
    #     response = Pets_api.update_pet_data(cls.id_pet, cls.name_category, cls.name_pet, cls.url_photo, cls.status, cls.tag_name)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_updating_pet_with_form_data(cls):
    #     '''Тест на обновления данных питомца с помощью form-data'''
    #     name_pet = 'Персик'
    #     status =  'pending'
    #     response = Pets_api.updating_pet_with_form_data(cls.id_pet,cls.name_pet,cls.status)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)
    #
    # @classmethod
    # def test_delete_pet(cls):
    #     '''Тест на удаление питомца из магазина'''
    #     response = Pets_api.delete_pet(cls.id_pet)
    #     required_fields = json.loads(response.text)
    #     Checking.check_all_required_fields(response, required_fields)
    #     Checking.check_status_code(response, 200)

# class Test_petstore():
#     '''Тестирование заказов зоомагазина'''
#
#     id_pet = 1
#     status = 'placed'   #Статус: placed, approved, delivered
#     count_pet = 3
#     order_number = 231
#
#     @classmethod
#     def test_place_order_pet(cls):
#         '''Тест на оформление заказа на питомца'''
#         response = Petstore_api.place_order_pet(cls.id_pet,cls.count_pet, cls.status, cls.order_number)
#         required_fields = json.loads(response.text)
#         Checking.check_all_required_fields(response, required_fields)
#         Checking.check_status_code(response, 200)
#
#     @classmethod
#     def test_search_order_number(cls):
#         '''Тест поиск заказа по его номеру'''
#         response = Petstore_api.search_order_number(cls.order_number)
#         required_fields = json.loads(response.text)
#         Checking.check_all_required_fields(response, required_fields)
#         Checking.check_status_code(response, 200)
#
#     @classmethod
#     def test_delete_by_order_number(cls):
#         '''Тест на удаление заказа по номеру '''
#         response = Petstore_api.delete_by_order_number(cls.order_number)
#         required_fields = json.loads(response.text)
#         Checking.check_all_required_fields(response, required_fields)
#         Checking.check_status_code(response, 200)

class Test_user():
    '''Тестирование пользователя зоомагазина'''
    user_name = 'QAJamesBraun'
    first_name = "James"
    last_name = "Braun"
    email = 'JamesBraun@mail.ru'
    password = 'qwerty123456'
    phone = '+123-1231-231'

    @classmethod
    def test_create_user(cls):
        '''Регистрация нового пользователя'''
        response = User.create_user(cls.user_name,cls.first_name, cls.last_name, cls.email, cls.password, cls.phone)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    def test_get_user_by_name(cls):
        '''Поиск пользователя по имени'''
        response = User.get_user_by_name(cls.user_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)
