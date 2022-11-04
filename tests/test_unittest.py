import unittest

from parameterized import parameterized

from main import YandexUser, TOKEN, host_create


class TestCreateFolder(unittest.TestCase):
    @parameterized.expand(
        [
            ("New folder", 201),
            ("Folder", 201),
            ("Folder 2", 201),
            ("Folder 2", 409)
        ],
    )
    def test_create_folder_ya(self, name, cod_answer): #проверяем, ответ после создания папки
        new_class = YandexUser(TOKEN)
        result = new_class.create_folder(name,host_create)
        self.assertEqual(result,cod_answer)

    @parameterized.expand(
        [
            ("New folder", 200),
            ("Folder", 200),
            ("Folder 2", 200),
        ],
    )
    def test_status_folder(self, name, cod_answer): #проверяем наличие папки
        new_class = YandexUser(TOKEN)
        result = new_class.get_status_files(name,host_create)
        self.assertEqual(result, cod_answer)