import requests
from Decorators_2 import logger

path = 'log_hero_intelligence.log'


@logger(path)
def hero_intelligence(heroes_list, link):
    data = link.json()
    dict = {}
    for heroe in data:
        if heroe['name'] in heroes_list:
            heroe_dict = {heroe['name']: heroe['powerstats']['intelligence']}
            intelligence_dict ={v: k for k, v in heroe_dict.items()}
            dict.update(intelligence_dict)
    return dict[max(dict)]


if __name__ == '__main__':
    list_ = ['Hulk', 'Thanos', 'Captain America']
    res = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    hero_intelligence(list_, res)