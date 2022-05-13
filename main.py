'''
Main script.
'''
import utils
import time


def main():
    
    NAME = 'Dani'
    player_id = utils.register(NAME)
    print(player_id)


    my_turn = utils.is_my_turn(player_id)

    while not my_turn:
        print('Zzz...')
        time.sleep(3)
        my_turn = utils.is_my_turn(player_id)
        
    print("It's my turn, continue in game...")


    print(my_turn)

    



if __name__ == '__main__':
    main()


