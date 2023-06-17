import requests

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Запрос на получение ссылки для загрузки файла
        params = {'path': '/72TlV-zhhRU.jpg', 'overwrite': 'true'}
        headers = {'Authorization': f'OAuth {token}'}
        response = requests.get(url, params=params, headers=headers)

        # Извлечение URL для загрузки файла
        href = response.json()['href']

        # Загрузка файла на Яндекс.Диск
        with open(path, 'rb') as f:
            response = requests.put(href, files={'file': f})

        # Проверка статуса загрузки файла
        if response.status_code == 201:
            print('Файл успешно загружен на Яндекс.Диск.')
        else:
            print('Произошла ошибка при загрузке файла на Яндекс.Диск.')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # URL для получения ссылки на загрузку файла
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    path_to_file = r'F:\фото\72TlV-zhhRU.jpg'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

