from utils.api_petstore import Petstore_api
class Test_petstore():
    '''Тестирование Зоомагазина'''

    def test_find_pet_by_status(self):
        '''Тест на поиск питомца по статусу'''
        response = Petstore_api.find_pet_by_status()