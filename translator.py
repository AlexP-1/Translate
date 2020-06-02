import requests
import json
import os
from pprint import pprint

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DISKURL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


def translate_it(file_inp, file_out, to_lang:'ru'):

    with open(file_inp, encoding='UTF-8') as fi:
        file_for_translate = fi.read()

    params = {
        'key': API_KEY,
        'text': file_for_translate,
        'lang': 'ru'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    pprint(json_['lang'])
    line = ''.join(json_['text'])

    with open(file_out, 'w', encoding='UTF-8') as fo:
        fo.write(line)


def upload_to_disk(file_name):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'OAuth AgAAAAA7LlbAAADLW2uUXegQwkg8qje0HgTqcEo'
    }

    params = {
        'path': os.path.join(file_name),
        'overwrite': 'True'
    }

    responce = requests.get(DISKURL, headers=headers, params=params)
    up_url = responce.json()['href']
    files = {'file': open(file_name, 'rb')}
    up_responce = requests.put(up_url, files=files)
    print(up_responce.status_code)
    files['file'].close()


translate_it('DE.txt', 'DE-RU.txt', 'ru')
upload_to_disk('DE-RU.txt')

translate_it('ES.txt', 'ES-RU.txt', 'ru')
upload_to_disk('ES-RU.txt')

translate_it('FR.txt', 'FR-RU.txt', 'ru')
upload_to_disk('FR-RU.txt')
