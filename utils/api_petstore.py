from utils.http_methods import Http_methods


base_url = 'https://petstore.swagger.io/v2'
dict_status = {'available' : 'Доступные питомцы',
               'pending' : 'Зарезервированные питомцы',
               'sold':'Проданные питомцы'}

class Petstore_api():
    '''API сайта Зоомагазин'''

    @staticmethod
    def find_pet_by_status():
        '''Найти питомцев по статусу (available, pending, sold)'''
        resource_get = '/pet/findByStatus'
        params = ('?status=')
        for i in dict_status.keys():
            url_get = f'{base_url}{resource_get}{params}{i}'
            result_get = Http_methods.get(url_get)
            print(f'СТАТУС: {dict_status[i]}\nПИТОМЦЫ: {result_get.text}\n-----\n')
        return result_get
