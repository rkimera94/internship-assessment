import os
import requests
from dotenv import load_dotenv
load_dotenv()

# get access token

access_token = os.environ.get('access_token')

# translate function


def translate_text(source_lang, target_lang, text):
    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": source_lang,
        "target_language": target_lang,
        "text": text
    }

    response = requests.post(
        f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        return translated_text

    else:
        print("Error:", response.status_code, response.text)


# list of valid languages
langs = ['English', 'Luganda', 'Runyankole', 'Ateso', 'Lugbara', 'Acholi']


def validateInputLang(lang):
    if lang in langs:
        return True
    else:
        return False


if __name__ == '__main__':

    # input source lang
    source_lang = input(
        'Please enter a source language:   ').capitalize().strip()
    while not validateInputLang(source_lang):
        print('Please choose a valid Language, From (English, Luganda, Runyankole, Ateso, Lugbara or Acholi)')
        source_lang = input(
            'Please enter a valid source language:   ').capitalize().strip()

    if source_lang == 'English' and validateInputLang(source_lang):
        # input target
        target_lang = input(
            'Please enter a target language:   ').capitalize().strip()
        while not validateInputLang(target_lang):
            print(
                'Please choose a valid Language, From (English, Luganda, Runyankole, Ateso, Lugbara or Acholi)')
            target_lang = input(
                'Please enter a valid target language:   ').capitalize().strip()

    else:
        # input target
        target_lang = 'English'


# enter text
get_trans_text = input('Enter text to translate: ')

# return translated text, call function to translate text

print('get_trans_text......', get_trans_text)

print(get_trans_text, '->', target_lang, ':',
      translate_text(source_lang, target_lang, get_trans_text))
