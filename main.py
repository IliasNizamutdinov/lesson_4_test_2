import requests

TOKEN = ''
host_create = 'https://cloud-api.yandex.net/v1/disk/resources/'

class YandexUser:
    def __init__(self, token):
        self.token = token
    def _get_headers_(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, name_folder: str, host: str):
        params = {"path": name_folder}
        resp = requests.put(host, headers = self._get_headers_(),params= params)
        return resp.status_code
    def get_status_files(self, name_folder: str, host: str):
        params = {"path": name_folder}
        resp = requests.get(host, headers = self._get_headers_(),params= params)
        return resp.status_code
if __name__ == '__main__':

    ya_client = YandexUser(TOKEN)
    name_folder = "Test folder"
    status_create = ya_client.create_folder(name_folder, host_create)

    if status_create == 201:
        print("Всё сделали!")
        status_create = ya_client.get_status_files(name_folder, host_create)
        if status_create == 200:
            print("Проверили, имеется!")
