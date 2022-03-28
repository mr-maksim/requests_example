import config
import requests


def get_intelligence(hero):
    intelligence_list = {}
    for name in hero:
        hero_req = requests.get(
            f'{config.BASE_URL}{config.TOKEN}/search/{name}').json()
        intelligence_list[name] = int(
            hero_req['results'][0]['powerstats'][('intelligence')])
    return intelligence_list


def cleverest(intelligence_dict):
    print("Герои в порядке убывания интелекта:")
    for num, sort in enumerate(sorted(intelligence_dict.items(), key=lambda x: x[1], reverse=True)):
        print(f'{num+1}) {sort[0]} - Интелект: {sort[1]}')


if __name__ == '__main__':
    hero = ['Hulk', 'Captain America', 'Thanos']
    cleverest(get_intelligence(hero))
