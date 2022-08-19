import requests
import re
import pprint
from collections import Counter
from json import dump as jdump

DOMAIN = 'https://api.hh.ru/'
url = f'{DOMAIN}vacancies'
key_word = input('Введите ключевое слово: ')
final_result = {'name': key_word}

params = {'text': f'{key_word}'}
result = requests.get(url, params=params)
data_json = result.json()
pages_count = data_json['pages']
vac_count = data_json['found']

final_result['pages'] = pages_count
final_result['vacancies_on_pages'] = vac_count


# pprint.pprint(data_json)

def calculation_of_the_average_salary(data_dic):
    global curr
    sum_salary = 0
    count_salary = 0
    none_count = 0

    for j in range(data_dic['pages']):
        params = {'text': f'{key_word}', 'page': j}
        data_dic = requests.get(url, params=params).json()

        for item in data_dic['items']:
            # TODO доделать конвертирование из разных валют
            curr_koeff = 1
            if item['salary'] == None:
                none_count += 1

            if item['salary'] is not None and (
                    item['salary']['currency'] == None or item['salary']['currency'] == 'RUR' or item['salary'][
                'currency'] == 'USD'):

                if item['salary']['currency'] == 'USD':
                    curr_koeff = 61

                if item['salary']['to'] is not None and item['salary']['from'] is not None:
                    sum_salary += ((item['salary']['to'] * curr_koeff + item['salary']['from'] * curr_koeff) / 2)
                    count_salary += 1
                elif item['salary']['to'] is not None:
                    sum_salary += (item['salary']['to']) * curr_koeff
                    count_salary += 1
                elif item['salary']['from'] is not None:
                    sum_salary += (item['salary']['from']) * curr_koeff
                    count_salary += 1

    return round(sum_salary / count_salary), count_salary, none_count


def analysis_requirements(data_dic):
    requirements_list = []

    for j in range(data_dic['pages']):
        params = {'text': f'{key_word}', 'page': j}
        data_dic = requests.get(url, params=params).json()

        for item in data_dic['items']:
            vak_res = requests.get(item['url']).json()
            if vak_res['key_skills'] is not None:
                for k in vak_res['key_skills']:
                    requirements_list.append(k['name'])

    # TODO посчитать в requirements_list сколько повторений и записать в словарь дле return
    return requirements_list


add = []
skills_with_counter = Counter(analysis_requirements(data_json))
for name, count in skills_with_counter.most_common(10):
    add.append({'name': name, 'count': count})

sal_tupl = calculation_of_the_average_salary(data_json)
final_result['RUR_and_USD_salary_find'] = sal_tupl[1]
final_result['NONE_salary_vac_find'] = sal_tupl[2]
final_result['average_salary'] = sal_tupl[0]
final_result['not_RUR_and_USA_salary_find'] = vac_count - sal_tupl[1] - sal_tupl[2]
final_result['skills'] = add



with open('resul.json', 'w') as f:
    jdump([final_result], f)
