import requests
import json
import os
import time

def text_to_speech(text='Hello'):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    url = "https://api.edenai.run/v2/audio/text_to_speech/"

    payload = {
        'providers': 'lovoai',
        'language': 'ru-RU',
        'option': 'FEMALE',
        'lovoai': 'ru-RU_Anna Kravchuk',
        'text': f'{text}'
    }

    response = requests.post(url,json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    with open(f'{unx_time}.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('lovoai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb')as file:
        file.write(r.content)

def main():
    text_to_speech(text= ' Вселенной, обслуживание его механизмов — ритуалами, вокруг которых возникла религия. Ученик офицера-жреца Хью Хойланд в столкновении с мутантами-мятежниками, таящимися в отдалённых закоулках Корабля, попадает в плен и становится компаньоном Джо-Джима Грегори — двухголового интеллектуала. Собрав небольшую команду, Хью постепенно постигает сущность мира вне Корабля, обнаруживает космическую шлюпку и совершает побег, приземлившись в финале на планету, пригодную для жизни.')

if __name__ == '__main__':
    main()