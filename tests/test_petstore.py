import json
from utils.api_petstore import Pets_api, Petstore_api, User
from utils.checking import Checking
import allure


@allure.epic('Тестирование питомцев')
class Test_pets():

    id_pet = 9223372016900015871
    name_category = 'Семейство обезьян'
    name_pet = 'King-Kong'
    url_photo = 'https://img.razrisyika.ru/kart/23/90336-king-kong-3.jpg'
    status = 'available'
    tag_name = 'Обезьяна'
    image = 'images/King-Kong.jpg'

    @classmethod
    @allure.description('Тест на поиск питомца по статусу')
    def test_find_pet_by_status(cls):
        response = Pets_api.find_pet_by_status(cls.status)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на добавление нового питомца')
    def test_add_new_pet(cls):
        response = Pets_api.add_new_pet(cls.id_pet, cls.name_category,cls.name_pet,cls.url_photo,cls.status,cls.tag_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на проверку питомца по ID')
    def test_search_pet_id(cls):
        response = Pets_api.search_pet_id(cls.id_pet)
        Checking.check_json_value(response, 'id',cls.id_pet)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на загрузку картинки питомца по id')
    def test_uploading_pet_image(cls):
        response = Pets_api.uploading_pet_image(cls.image,'jpeg', cls.id_pet)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на обновления данных существующего питомца')
    def test_update_pet_data(cls):
        name_category = 'Семейство кошачьих'
        name_pet = 'Персик'
        tag_name = 'Кот'
        url_photo = 'https://www.purina.ru/sites/default/files/2021-10/amer-korotkoserst-2.jpg'
        response = Pets_api.update_pet_data(cls.id_pet, name_category, name_pet, url_photo, cls.status, tag_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на обновления данных питомца с помощью form-data')
    def test_updating_pet_with_form_data(cls):
        name_pet = 'Персик'
        status =  'pending'
        response = Pets_api.updating_pet_with_form_data(cls.id_pet,name_pet,status)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)
#
    @classmethod
    @allure.description('Тест на удаление питомца из магазина')
    def test_delete_pet(cls):
        response = Pets_api.delete_pet(cls.id_pet)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

@allure.epic('Тестирование заказов зоомагазина')
class Test_petstore():

    id_pet = 1
    status = 'placed'   #Статус: placed, approved, delivered
    count_pet = 3
    order_number = 231

    @classmethod
    @allure.description('Тест на оформление заказа на питомца')
    def test_place_order_pet(cls):
        response = Petstore_api.place_order_pet(cls.id_pet,cls.count_pet, cls.status, cls.order_number)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест поиск заказа по его номеру')
    def test_search_order_number(cls):
        response = Petstore_api.search_order_number(cls.order_number)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на удаление заказа по номеру')
    def test_delete_by_order_number(cls):
        response = Petstore_api.delete_by_order_number(cls.order_number)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

@allure.epic('Тестирование пользователя зоомагазина')
class Test_user():

    user_name = 'QAJamesBraun'
    first_name = "James"
    last_name = "Braun"
    email = 'JamesBraun@mail.ru'
    password = 'qwerty123456'
    phone = '+123-1231-231'

    @classmethod
    @allure.description('Регистрация нового пользователя')
    def test_create_user(cls):
        response = User.create_user(cls.user_name,cls.first_name, cls.last_name, cls.email, cls.password, cls.phone)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Поиск пользователя по имени')
    def test_get_user_by_name(cls):
        response = User.get_user_by_name(cls.user_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @allure.description('Создание новых пользователей')
    def test_create_lst_user(sels):
        response = User.create_lst_user()
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест изменения данных существующего пользователя по User name')
    def test_update_user_by_user_name(cls):
        response = User.update_user_by_user_name(cls.user_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Поиск пользователя по имени')
    def test_get_user_by_name2(cls):
        response = User.get_user_by_name(cls.user_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на авторизация пользователя в системе')
    def test_login(cls):
        response = User.login(cls.user_name,cls.password)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @allure.description('Тест выход пользователя из текущего сеанса')
    def test_logout(self):
        response = User.logout()
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)

    @classmethod
    @allure.description('Тест на удаления пользователя')
    def test_delete_user(cls):
        response = User.delete_user(cls.user_name)
        required_fields = json.loads(response.text)
        Checking.check_all_required_fields(response, required_fields)
        Checking.check_status_code(response, 200)
