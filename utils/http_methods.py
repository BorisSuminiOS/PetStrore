import requests

headers = {'Content-Type':'application/json'}
cookies = ''

class Http_methods():
    '''HTTP методы'''
    @staticmethod
    def get(url):
        result_get = requests.get(url, headers=headers, cookies=cookies)
        return result_get

    @staticmethod
    def post(url, body):
        result_post = requests.post(url, json=body, headers=headers, cookies=cookies)
        return result_post

    @staticmethod
    def put(url, body):
        result_put = requests.put(url, json=body, headers=headers, cookies=cookies)
        return result_put

    @staticmethod
    def delete(url, body):
        result_delete = requests.delete(url, json=body, headers=headers, cookies=cookies)
        return result_delete

