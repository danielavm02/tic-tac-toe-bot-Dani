'''
Utils module.
'''


import requests


def register(name: str) -> str: 
    response = requests.post("http://127.0.0.1:8000/register_player/"+name)
    print(response.json())
    player_id = response.json()      # TODO: implement API call
    return player_id


def is_my_turn(player_id: str) -> bool:

    my_turn = True          # TODO: implement API call
    return my_turn


