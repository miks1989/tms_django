import requests
from bs4 import BeautifulSoup


# def parser_gorodkotlov(link):
#     if link:
#         try:
#             responce = requests.get(link).text
#             soup = BeautifulSoup(responce, "lxml")
#             result = float(soup.find('span', class_='price_value').text.replace(" ", ""))
#             return result
#         except requests.exceptions.SSLError:
#             return None
#     else:
#         return None
#
# parser_gorodkotlov('https://cyclone.by/catalog/kotly/tverdotoplivnye/tverdotoplivnyy-kotel-tis-plus-15/')

def parser_ktl(link):
    if link:
        responce = requests.get(link).text
        print(responce)
        soup = BeautifulSoup(responce, "lxml")
        result = soup.find('span', {'itemprop': 'lowPrice'}).text
        print(result)
        result = float(soup.find('span', {'itemprop': 'lowPrice'}).text[:-2])
        return result
    else:
        return None

print(parser_ktl('https://ktl.by/otopitelnoe-oborudovanie/kotly-tverdotoplivnye/tverdotoplivnyy-kotel-tis-plus-15'))