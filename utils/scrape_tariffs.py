import json

import aiohttp


async def scrape_tariffs_func(price, internet, time, connect_type, loyalty_input):
    url = f'https://www.lifecell.ua/products/api/v1/tariffs/active?id=3,4,8,9,10,11,12,14,15,16,17,18,19,20,21,23,' \
          f'37&regions=6409,1428,164,14,1&'
    if price != '_':
        url += f'measurement=gigabytes:{internet}&'
    if internet != '_':
        url += f'measurement=minutes:{time}&'
    if time != '_':
        url += f'measurement=price:{price}&'
    if connect_type != '_':
        url += f'tariff_types={connect_type}&'
    if loyalty_input != '_':
        url += f'tariff_loyalties={loyalty_input}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                data = await response.json()
                text = ''
                if data:
                    for item in data:
                        text += f"📱|Доступні тарифи по вашим параметрам:\n {item['name']}:\n{item['shop_link_url']}\n\n"
                else:
                    return 'По заданним параметрам тарифів немає!'
                return text
            except (json.JSONDecodeError, aiohttp.ContentTypeError):
                print('Ошибка при разборе JSON-ответа')
