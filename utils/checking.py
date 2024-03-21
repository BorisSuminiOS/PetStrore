from requests import Response
class Checking():
    '''Проверки ответов от сервера'''

    @staticmethod
    def check_status_code(response: Response, status_code):
        status_code_response = response.status_code
        assert status_code_response == status_code
        print(f'СТАТУС КОД СООТВЕТСТВУЕТ: {status_code_response}\n')

