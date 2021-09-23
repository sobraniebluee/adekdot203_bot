import random
import json

def openJson(anekdot_type):
    with open(f'json/json_anekdots_{anekdot_type}.json','r',encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data

def randomAnekdot(anekdotType):
    randomItem = random.choice(openJson(anekdotType))
    return randomItem['anekdot']
