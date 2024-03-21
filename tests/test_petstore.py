from utils.api_petstore import Petstore_api

lst_status_pets = ['available', 'pending', 'sold']
class Test_petstore():
    '''Тестирование Зоомагазина'''

    def test_find_pet_by_status(self):
        '''Тест на поиск питомца по статусу'''
        for i in lst_status_pets:
            response = Petstore_api.find_pet_by_status(i)