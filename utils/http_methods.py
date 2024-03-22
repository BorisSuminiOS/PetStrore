import requests
from utils.logger import Logger

headers = {'Content-Type':'application/json'}
cookies = ''

class Http_methods():
    '''HTTP методы'''
    @staticmethod
    def get(url):
        Logger.add_request(url, "GET")
        result_get = requests.get(url, headers=headers, cookies=cookies)
        Logger.add_response(result_get)
        return result_get

    @staticmethod
    def post(url, body):
        Logger.add_request(url, "POST")
        result_post = requests.post(url, json=body, headers=headers, cookies=cookies)
        Logger.add_response(result_post)
        return result_post

    @staticmethod
    def put(url, body):
        Logger.add_request(url, "PUT")
        result_put = requests.put(url, json=body, headers=headers, cookies=cookies)
        Logger.add_response(result_put)
        return result_put

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, "DELETE")
        result_delete = requests.delete(url, json=body, headers=headers, cookies=cookies)
        Logger.add_response(result_delete)
        return result_delete

