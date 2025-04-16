#Max Holdaway Coin Change Problem: Coin Change function(s)
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import NumberValidator
import copy

#This counts the amount of coins (varying by country) inside a specifc value
def count_coins(coin_value_list):
    #Little inner function that is a user input for the specific country
    def get_country():
        country = inquirer.select(message='Which currency are you counting coins for?:', choices=['United States', 'Europe', 'Britain', 'Japan', 'China']).execute()
        return country
    #Inner function that gets the amount of money to coin change also servers as my user input validiation and edge testing
    def get_coin_amount(coin_type):
        while True:
            amount = str(inquirer.text(message=f'How many {coin_type} do you have? (will get auto rounded to two decimals (unless you do japanese currency then it will be rounded to integers)):').execute())
            if amount.isnumeric():
                amount = int(amount)
                if amount >= 0 and amount != 0:
                    return amount
                else:
                    print("No negative numbers those don't work with coins. And if you put zero that also doesn't work with coins.")
            else:
                try:
                    amount = float(amount)
                    if amount >= 0 and amount != 0:
                        return amount
                    else:
                        print("No negative numbers those don't work with coins. And if you put zero that also doesn't work with coins.")
                except:
                    print("Please type in a number (you can include decimals).")
    user_country = get_country()
    if user_country == 'United States':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'US':
                US_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Dollars'
        dollar_coin_amount = 0
        quarter_amount = 0
        dime_amount = 0
        nickel_amount = 0
        penny_amount = 0
        user_amount = round(get_coin_amount(coin_type), 2)
        total_amount = copy.copy(user_amount)
        #A while loop to find all the coins inside the specific amount of a currency (varying by country but this system is used for all of them)
        while user_amount > 0:
            user_amount = round(user_amount, 2)
            if user_amount >= US_dict['dollar_coin']['coin_value']:
                user_amount -= US_dict['dollar_coin']['coin_value']
                dollar_coin_amount += 1
            elif user_amount >= .25:
                user_amount -= US_dict['quarter']['coin_value']
                quarter_amount += 1
            elif user_amount >= .10:
                user_amount -= US_dict['dime']['coin_value']
                dime_amount += 1
            elif user_amount >= .05:
                user_amount -= US_dict['nickel']['coin_value']
                nickel_amount += 1
            elif user_amount >= 0.01:
                user_amount -= US_dict['penny']['coin_value']
                penny_amount += 1
        print(f'From your total amount {total_amount} there was:')
        print(f'This many dollar coins: {dollar_coin_amount}')
        print(f'This many quarters: {quarter_amount}')
        print(f'This many dimes: {dime_amount}')
        print(f'This many nickels: {nickel_amount}')
        print(f'This many pennys: {penny_amount}')
    elif user_country == 'Europe':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'EU':
                EU_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Euros'
        two_euro_amount = 0
        one_euro_amount = 0
        fifty_euro_cent_amount = 0
        twenty_euro_cent_amount = 0
        ten_euro_cent_amount = 0
        five_euro_cent_amount = 0
        two_euro_cent_amount = 0
        one_euro_cent_amount = 0
        user_amount = round(get_coin_amount(coin_type), 2)
        total_amount = copy.copy(user_amount)
        while user_amount > 0 and user_amount != 0:
            user_amount = round(user_amount, 2)
            if user_amount >= 2:
                user_amount -= EU_dict['two_euros']['coin_value']
                two_euro_amount += 1
            elif user_amount <= 1.99 and user_amount >= 1:
                user_amount -= EU_dict['one_euro']['coin_value']
                one_euro_amount
            elif user_amount <= .99 and user_amount >= .50:
                user_amount -= EU_dict['fifty_euro_cent']['coin_value']
                fifty_euro_cent_amount += 1
            elif user_amount <= .49 and user_amount >= .20:
                user_amount -= EU_dict['twenty_euro_cent']['coin_value']
                twenty_euro_cent_amount += 1
            elif user_amount <= .19 and user_amount >= .10:
                user_amount -= EU_dict['ten_euro_cent']['coin_value']
                ten_euro_cent_amount += 1
            elif user_amount <= .09 and user_amount >= .05:
                user_amount -= EU_dict['five_euro_cent']['coin_value']
                five_euro_cent_amount += 1
            elif user_amount <= .04 and user_amount >= .02:
                user_amount -= EU_dict['two_euro_cent']['coin_value']
                two_euro_cent_amount += 1
            elif user_amount < .02  and user_amount != 0:
                user_amount -= EU_dict['one_euro_cent']['coin_value']
                one_euro_cent_amount += 1
        print(f'From your total amount {total_amount} there was:')
        print(f'This many two euro coins: {two_euro_amount}')
        print(f'This many one euro coins: {one_euro_amount}')
        print(f'This many fifty euro cent coins: {fifty_euro_cent_amount}')
        print(f'This many twenty euro cent coins: {twenty_euro_cent_amount}')
        print(f'This many ten euro cent coins: {ten_euro_cent_amount}')
        print(f'This many five euro cent coins: {five_euro_cent_amount}')
        print(f'This many two euro cent coins: {two_euro_cent_amount}')
        print(f'This many one euro cent coins: {one_euro_cent_amount}')
    elif user_country == 'Britain':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'BR':
                BR_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Pounds'
        two_pound_amount = 0
        one_pound_amount = 0
        fifty_pence_amount = 0
        twenty_pence_amount = 0
        ten_pence_amount = 0
        five_pence_amount = 0
        two_pence_amount = 0
        one_pence_amount = 0
        user_amount = round(get_coin_amount(coin_type), 2)
        total_amount = copy.copy(user_amount)
        while user_amount > 0 and user_amount != 0:
            user_amount = round(user_amount, 2)
            if user_amount >= 2:
                user_amount -= BR_dict['two_pounds']['coin_value']
                two_pound_amount += 1
            elif user_amount <= 1.99 and user_amount >= 1:
                user_amount -= BR_dict['one_pound']['coin_value']
                one_pound_amount
            elif user_amount <= .99 and user_amount >= .50:
                user_amount -= BR_dict['fifty_pence']['coin_value']
                fifty_pence_amount += 1
            elif user_amount <= .49 and user_amount >= .20:
                user_amount -= BR_dict['twenty_pence']['coin_value']
                twenty_pence_amount += 1
            elif user_amount <= .19 and user_amount >= .10:
                user_amount -= BR_dict['ten_pence']['coin_value']
                ten_pence_amount += 1
            elif user_amount <= .09 and user_amount >= .05:
                user_amount -= BR_dict['five_pence']['coin_value']
                five_pence_amount += 1
            elif user_amount <= .04 and user_amount >= .02:
                user_amount -= BR_dict['two_pence']['coin_value']
                two_pence_amount += 1
            elif user_amount > 0:
                user_amount -= BR_dict['one_pence']['coin_value']
                one_pence_amount += 1
        print(f'From your total amount {total_amount} there was:')
        print(f'This many two pound coins: {two_pound_amount}')
        print(f'This many one pound coins: {one_pound_amount}')
        print(f'This many fifty pence coins: {fifty_pence_amount}')
        print(f'This many twenty pence coins: {twenty_pence_amount}')
        print(f'This many ten pence coins: {ten_pence_amount}')
        print(f'This many five pence coins: {five_pence_amount}')
        print(f'This many two pence coins: {two_pence_amount}')
        print(f'This many one pence coins: {one_pence_amount}')
    elif user_country == 'Japan':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'JP':
                JP_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Yens'
        one_yen_amount = 0
        five_yen_amount = 0
        ten_yen_amount = 0
        fifty_yen_amount = 0
        one_hundred_yen_amount = 0
        five_hundred_yen_amount = 0
        user_amount = round(get_coin_amount(coin_type), 0)
        total_amount = copy.copy(user_amount)
        while user_amount > 0 and user_amount != 0:
            user_amount = round(user_amount, 0)
            if user_amount >= 500:
                user_amount -= JP_dict['five_hundred_yen']['coin_value']
                five_hundred_yen_amount += 1
            elif user_amount <= 499 and user_amount >= 100:
                user_amount -= JP_dict['hundred_yen']['coin_value']
                one_hundred_yen_amount += 1
            elif user_amount <= 99 and user_amount >= 50:
                user_amount -= JP_dict['fifty_yen']['coin_value']
                fifty_yen_amount += 1
            elif user_amount <= 49 and user_amount >= 10:
                user_amount -= JP_dict['ten_yen']['coin_value']
                ten_yen_amount += 1
            elif user_amount <= 9 and user_amount >= 5:
                user_amount -= JP_dict['five_yen']['coin_value']
                five_yen_amount += 1
            elif user_amount >= 1:
                user_amount -= JP_dict['one_yen']['coin_value']
                one_yen_amount += 1
        print(f'From your total amount {total_amount} there was:')
        print(f'This many five hundred yen coins: {five_hundred_yen_amount}')
        print(f'This many one hundred yen coins: {one_hundred_yen_amount}')
        print(f'This many fifty yen coins: {fifty_yen_amount}')
        print(f'This many ten yen coins: {ten_yen_amount}')
        print(f'This many five yen coins: {five_yen_amount}')
        print(f'This many one yen coins: {one_yen_amount}')
    elif user_country == 'China':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'CH':
                CH_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Yuans'
        one_fen_amount = 0
        two_fen_amount = 0
        five_fen_amount = 0
        one_jiao_amount = 0
        two_jiao_amount = 0
        five_jiao_amount = 0
        one_yuan_amount = 0
        user_amount = round(get_coin_amount(coin_type), 2)
        total_amount = copy.copy(user_amount)
        while user_amount > 0 and user_amount != 0:
            user_amount = round(user_amount, 2)
            if user_amount >= 1:
                user_amount -= CH_dict['one_yuan']['coin_value']
                one_yuan_amount += 1
            elif user_amount <= .99 and user_amount >= .50:
                user_amount -= CH_dict['five_jiao']['coin_value']
                five_jiao_amount += 1
            elif user_amount <= .49 and user_amount >= .20:
                user_amount -= CH_dict['two_jiao']['coin_value']
                two_jiao_amount += 1
            elif user_amount <= .19 and user_amount >= .10:
                user_amount -= CH_dict['one_jiao']['coin_value']
                one_jiao_amount += 1
            elif user_amount <= .09 and user_amount >= .05:
                user_amount -= CH_dict['five_fen']['coin_value']
                five_fen_amount += 1
            elif user_amount <= .04 >= .02:
                user_amount -= CH_dict['two_fen']['coin_value']
                two_fen_amount += 1
            elif user_amount < .02 and user_amount != 0:
                user_amount -= CH_dict['one_fen']['coin_value']
                one_fen_amount += 1
        print(f'From your total amount {total_amount} there was:')
        print(f'This many one yuan coins: {one_yuan_amount}')
        print(f'This many five jiao coins: {five_jiao_amount}')
        print(f'This many two jiao coins: {two_jiao_amount}')
        print(f'This many one jiao coins: {one_jiao_amount}')
        print(f'This many five fen coins: {five_fen_amount}')
        print(f'This many two fen coins: {two_fen_amount}')
        print(f'This many one fen coins: {one_fen_amount}')
