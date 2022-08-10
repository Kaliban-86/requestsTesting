import requests
import pprint

DOMAIN = 'https://api.hh.ru/'
url = f'{DOMAIN}vacancies'
key_word = input('Введите ключевое слово: ')

params = {'text': f'{key_word}'}
result = requests.get(url, params=params)
data_json = result.json()

# pprint.pprint(data_json)

print(type(data_json), len(data_json), data_json.keys())
print(data_json['items'][0]['snippet']['requirement'])

print('Всего страниц: ', data_json['pages'])
print('Длина - ', len(data_json['items']), 'Тип -', type(data_json['items']))


def calculation_of_the_average_salary(data_dic):
    sum_salary = 0
    count_salary = 0

    for j in range(data_dic['pages'] - 1):
        params = {'text': f'{key_word}', 'page': j}
        data_dic = requests.get(url, params=params).json()

        for item in data_dic['items']:
            # TODO доделать конвертирование из разных валют
            if item['salary'] is not None:
                if item['salary']['to'] is not None and item['salary']['from'] is not None:
                    sum_salary += (item['salary']['to'] + item['salary']['from']) / 2
                    count_salary += 1
                elif item['salary']['to'] is not None:
                    sum_salary += item['salary']['to']
                    count_salary += 1
                elif item['salary']['from'] is not None:
                    sum_salary += item['salary']['from']
                    count_salary += 1
    return round(sum_salary / count_salary)


def analysis_requirements(data_dic):
    requirements_list = []

    for j in range(data_dic['pages'] - 1):
        params = {'text': f'{key_word}', 'page': j}
        data_dic = requests.get(url, params=params).json()

        for item in data_dic['items']:
            # TODO  отпарсить на какие-то конкретные требования
            if item['snippet']['requirement'] is not None:
                requirements_list.append(item['snippet']['requirement'])

    # TODO посчитать в requirements_list сколько повторений и записать в словарь дле return

# print(calculation_of_the_average_salary(data_json))
