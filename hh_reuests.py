import requests
import pprint

DOMAIN = 'https://api.hh.ru/'
url = f'{DOMAIN}vacancies'
key_word = input('Введите ключевое слово: ')

params = {
    'text': f'{key_word}',
    'page': 1
}
result = requests.get(url, params=params)
print(result.status_code)
data_json = result.json()

# pprint.pprint(data_json)
#
# print(len(data_json), type(data_json))
# for i in data_json:
#     print(i, ' - ', type(data_json[i]))

print('Всего страниц: ', data_json['pages'])
print('Длина - ', len(data_json['items']), 'Тип -', type(data_json['items']))

sum_salary = 0
count_salary = 0
for i in data_json['items']:
    #TODO доделать конвертирование из разных валют

    if i['salary'] is not None:
        if i['salary']['to'] is not None and i['salary']['from'] is not None:
            sum_salary += (i['salary']['to'] + i['salary']['from']) / 2
            count_salary += 1
        elif i['salary']['to'] is not None:
            sum_salary += i['salary']['to']
            count_salary += 1
        elif i['salary']['from'] is not None:
            sum_salary += i['salary']['from']
            count_salary += 1

print(sum_salary / count_salary)
