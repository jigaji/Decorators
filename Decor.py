from datetime import datetime
import requests

url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes = ['Hulk', 'Captain America', 'Thanos']
log_path = 'logger.txt'

def logger(path):
    def foo(old_function):
        def new_function(*args, **kwargs):
            date_of_function = datetime.now().strftime('%d %m %y - %H:%M:%S')
            print('Дата и время вызова функции', date_of_function)
            print('имя функции', old_function.__name__)
            print('аргументы функции', args, kwargs)
            result = old_function(*args, **kwargs)
            print('результат функции', result)
            line = f'Дата и время вызова функции- {date_of_function} \n' \
                   f'имя функции - {old_function.__name__}\n' \
                   f'аргументы функции - {args}, {kwargs}\n' \
                   f'результат функции - {result}'
            with open(path, 'w', encoding='utf-8') as file:
                file.write(line)
            return result
        return new_function
    return foo
logger_1 = logger(log_path)
@logger_1
def the_smartest():
    intel = {}
    for hero in heroes:
        hero_r = requests.get(url + hero)
        response = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
        intel[hero] = response
    smart = max(intel.items(), key=lambda x: x[1])
    return f'Самый умный из героев - {smart[0]} (не зря у него перчатка бесконечности)'

@logger_1
def square(a, b):
    return a * b


the_smartest()
print('_________________________')
square(8, 4)






