#Max Holdaway Coin Change Problem: Main Function / User Interface
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import coin_change as coin_conversion_functions
import coin_load as coin_load_functions

def main():
    coin_value_list = coin_load_functions.load_coin_values(coin_value_list=[])
    while True:
        user_input = inquirer.select(message='What do you want to do?:', choices=['Coin Change', 'Exit']).execute()
        if user_input == 'Coin Change':
            coin_conversion_functions.count_coins(coin_value_list)
            continue
        elif user_input == 'Exit':
            print("Hope this coin change program was useful goodbye!")
            break

main()
