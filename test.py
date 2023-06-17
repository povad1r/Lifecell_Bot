import requests

url = 'https://www.lifecell.ua/products/api/v1/tariffs/active?id=3,4,8,9,10,11,12,14,15,16,17,18,19,20,21,23,37&regions=6409,1428,164,14,1&measurement=minutes:lte_300'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
    print(response)
else:
    print(f'Ошибка при выполнении запроса: {response.status_code}')