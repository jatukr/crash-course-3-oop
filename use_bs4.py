import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
status = requests.get(url)
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        #print(f'Content {response.content}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Woopss ada kesalahan {response.status_code}')
except Exception as e:
    print('There is an Error', e)
print('Program End')