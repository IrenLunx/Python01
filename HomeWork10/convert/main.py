# Конвертер валют:
# Приложение для вывода текущего курса валют (валюты выбирайте любые). 
# Постарайтесь сделать конвертер валют (Например, ввел в рублях, получил в $). 
# Было бы классно обернуть все в графический интерфейс.

import requests
from bs4 import BeautifulSoup

Dollar_Rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
Eur_Rub = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=vpL_YrG2N5OQwPAPrbGzkAE&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAEYADIMCAAQsQMQQxBGEIICMgcIABCxAxBDMgQIABBDMggIABCABBCxAzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIHCAAQyQMQQ0oECEEYAEoECEYYAFAAWABg3RBoAHABeACAAcEBiAHyApIBAzAuMpgBAKABAcABAQ&sclient=gws-wiz'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

def dollar_rub():
    full_pars = requests.get(Dollar_Rub, headers=headers)
    soup_pars = BeautifulSoup(full_pars.content, 'html.parser')
    convert_D_R = soup_pars.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
    result = str(convert_D_R[0].text)
    result = float(result.replace(',', '.'))
    return result

def eur_rub():
    full_pars = requests.get(Eur_Rub, headers=headers)
    soup_pars = BeautifulSoup(full_pars.content, 'html.parser')
    convert_E_R = soup_pars.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
    result = str(convert_E_R[0].text)
    result = float(result.replace(',', '.'))
    return result

# print('Перевод из доллара в рубль - 1')
# print('Перевод из рубля в доллар - 2')
# print('Перевод из евро в рубль - 3')
# print('Перевод из рубля в евро - 4')
# val = float(input('Введите число: '))
# countVal = float(input('Введите число для перевода: '))
# match val:
#     case 1: 
#         result = dollar_rub()
#         result *= countVal
#         print(result)
#     case 2:
#         result = dollar_rub()
#         result = countVal / result
#         print(result)
#     case 3:
#         result = eur_rub()
#         result *= countVal
#         print(result)
#     case 4:
#         result = eur_rub()
#         result = countVal / result
#         print(result)