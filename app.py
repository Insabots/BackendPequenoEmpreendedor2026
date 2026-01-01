import requests

answare = requests.get('https://youtube.com')

if answare.status_code == 200:
    print(f'Your request has been complete')
else:
    print(f'your request failed with statuts code: {answare.status_code}')


