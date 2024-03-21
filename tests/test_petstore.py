import json

from utils.api_petstore import Petstore_api
from utils.checking import Checking

lst_status_pets = ['available', 'pending', 'sold']
class Test_petstore():
    '''Тестирование Зоомагазина'''

    def test_find_pet_by_status(self):
        '''Тест на поиск питомца по статусу'''
        for i in lst_status_pets:
            response = Petstore_api.find_pet_by_status(i)
            required_fields = json.loads(response.text)
            Checking.check_required_fields(response, required_fields)
            Checking.check_status_code(response, 200)