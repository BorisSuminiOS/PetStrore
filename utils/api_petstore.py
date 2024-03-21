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
        print(f'СТАТУС: {status}\nПИТОМЦЫ: {result_get.text}\n-----\n')
        return result_get


