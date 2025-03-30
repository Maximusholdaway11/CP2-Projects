#Max Holdaway Coin Change Problem: Coin Change function(s)
import csv
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import NumberValidator
import copy

def load_coin_values(coin_value_list):
    with open("coin_change_problem/coin_values.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == 'US':
                penny_split = row[1].split('-')
                penny_value = {'coin_name': 'Penny', 'coin_value': float(penny_split[1])}
                nickel_split = row[2].split('-')
                nickel_value = {'coin_name': 'Nickel', 'coin_value': float(nickel_split[1])}
                dime_split = row[3].split('-')
                dime_value = {'coin_name': 'Dime', 'coin_value': float(dime_split[1])}
                quarter_split = row[4].split('-')
                quarter_value ={'coin_name': 'Quarter', 'coin_value': float(quarter_split[1])}
                dollar_split = row[5].split('-')
                dollar_value = {'coin_name': 'Dollar Coin', 'coin_value': float(dollar_split[1])}
                us_coin_values_dict = {'penny': penny_value, 'nickel': nickel_value, 'dime': dime_value, 'quarter': quarter_value, 'dollar_coin': dollar_value, 'country': 'US'}
                coin_value_list.append(us_coin_values_dict)
            elif row[0] == 'EU':
                euro_cent_one_split = row[1].split('-')
                euro_cent_one_value = {'coin_name': 'One Euro Cent', 'coin_value': float(euro_cent_one_split[1])}
                euro_cent_two_split = row[2].split('-')
                euro_cent_two_value = {'coin_name': 'Two Euro Cents', 'coin_value': float(euro_cent_two_split[1])}
                euro_cent_five_split = row[3].split('-')
                euro_cent_five_value = {'coin_name': 'Five Euro Cents', 'coin_value': float(euro_cent_five_split[1])}
                euro_cent_ten_split = row[4].split('-')
                euro_cent_ten_value ={'coin_name': 'Ten Euro Cents', 'coin_value': float(euro_cent_ten_split[1])}
                euro_cent_twenty_split = row[5].split('-')
                euro_cent_twenty_value = {'coin_name': 'Twenty Euro Cents', 'coin_value': float(euro_cent_twenty_split[1])}
                euro_cent_fifty_split = row[6].split('-')
                euro_cent_fifty_value = {'coin_name': 'Fifty Euro Cents', 'coin_value': float(euro_cent_fifty_split[1])}
                euro_one_split = row[7].split('-')
                euro_one_value = {'coin_name': 'One Euro', 'coin_value': float(euro_one_split[1])}
                euro_two_split = row[8].split('-')
                euro_two_value = {'coin_name': 'Two Euros', 'coin_value': float(euro_two_split[1])}
                eu_coin_values_dict = {'one_euro_cent': euro_cent_one_value, 'two_euro_cent': euro_cent_two_value, 'five_euro_cent': euro_cent_five_value, 'ten_euro_cent': euro_cent_ten_value, 'twenty_euro_cent': euro_cent_twenty_value, 'fifty_euro_cent': euro_cent_fifty_value, 'one_euro': euro_one_value, 'two_euros': euro_two_value, 'country': 'EU'}
                coin_value_list.append(eu_coin_values_dict)
            elif row[0] == 'BR':
                pence_one_split = row[1].split('-')
                pence_one_value = {'coin_name': 'One Pence', 'coin_value': float(pence_one_split[1])}
                pence_two_split = row[2].split('-')
                pence_two_value = {'coin_name': 'Two Pences', 'coin_value': float(pence_two_split[1])}
                pence_five_split = row[3].split('-')
                pence_five_value = {'coin_name': 'Five Pences', 'coin_value': float(pence_five_split[1])}
                pence_ten_split = row[4].split('-')
                pence_ten_value ={'coin_name': 'Ten Pences', 'coin_value': float(pence_ten_split[1])}
                pence_twenty_split = row[5].split('-')
                pence_twenty_value = {'coin_name': 'Twenty Pences', 'coin_value': float(pence_twenty_split[1])}
                pence_fifty_split = row[6].split('-')
                pence_fifty_value = {'coin_name': 'Fifty Pences', 'coin_value': float(pence_fifty_split[1])}
                pound_one_split = row[7].split('-')
                pound_one_value = {'coin_name': 'One Pound', 'coin_value': float(pound_one_split[1])}
                pound_two_split = row[8].split('-')
                pound_two_value = {'coin_name': 'Two Pounds', 'coin_value': float(pound_two_split[1])}
                br_coin_values_dict = {'one_pence': pence_one_value, 'two_pence': pence_two_value, 'five_pence': pence_five_value, 'ten_pence': pence_ten_value, 'twenty_pence': pence_twenty_value, 'fifty_pence': pence_fifty_value, 'one_pound': pound_one_value, 'two_pounds': pound_two_value, 'country': 'BR'}
                coin_value_list.append(br_coin_values_dict)
            elif row[0] =='JP':
                one_yen_split = row[1].split('-')
                one_yen_value = {'coin_name': 'One Yen', 'coin_value': float(one_yen_split[1])}
                five_yen_split = row[2].split('-')
                five_yen_value = {'coin_name': 'Five Yen', 'coin_value': float(five_yen_split[1])}
                ten_yen_split = row[3].split('-')
                ten_yen_value = {'coin_name': 'Ten Yen', 'coin_value': float(ten_yen_split[1])}
                fifty_yen_split = row[4].split('-')
                fifty_yen_value ={'coin_name': 'Fifty Yen', 'coin_value': float(fifty_yen_split[1])}
                hundred_yen_split = row[5].split('-')
                hundred_yen_value = {'coin_name': 'One Hundred Yen', 'coin_value': float(hundred_yen_split[1])}
                five_hundred_yen_split = row[6].split('-')
                five_hundred_yen_value = {'coin_name': 'Five Hundred Yen', 'coin_value': float(five_hundred_yen_split[1])}
                jp_coin_values_dict = {'one_yen': one_yen_value, 'five_yen': five_yen_value, 'ten_yen': ten_yen_value, 'fifty_yen': fifty_yen_value, 'hundred_yen': hundred_yen_value, 'five_hundred_yen': five_hundred_yen_value, 'country': 'JP'}
                coin_value_list.append(jp_coin_values_dict)
            elif row[0] == 'CH':
                one_fen_split = row[1].split('-')
                one_fen_value = {'coin_name': 'One Fen', 'coin_value': float(one_fen_split[1])}
                five_fen_split = row[2].split('-')
                five_fen_value = {'coin_name': 'Five Yen', 'coin_value': float(five_fen_split[1])}
                one_jiao_split = row[3].split('-')
                one_jiao_value = {'coin_name': 'Ten Yen', 'coin_value': float(one_jiao_split[1])}
                two_jiao_split = row[4].split('-')
                two_jiao_value ={'coin_name': 'Fifty Yen', 'coin_value': float(two_jiao_split[1])}
                five_jiao_split = row[5].split('-')
                five_jiao_value = {'coin_name': 'One Hundred Yen', 'coin_value': float(five_jiao_split[1])}
                one_yuan_split = row[6].split('-')
                one_yuan_value = {'coin_name': 'Five Hundred Yen', 'coin_value': float(one_yuan_split[1])}
                ch_coin_values_dict = {'one_fen': one_fen_value, 'five_fen': five_fen_value, 'one_jiao': one_jiao_value, 'two_jiao': two_jiao_value, 'five_jiao': five_jiao_value, 'one_yuan': one_yuan_value, 'country': 'CH'}
                coin_value_list.append(ch_coin_values_dict)
        return coin_value_list

def count_coins(coin_value_list):
    def get_country():
        country = inquirer.select(message='Which currency are you counting coins for?:', choices=['United States', 'Europe', 'Britain', 'Japan', 'China']).execute()
        return country
    def get_coin_amount(coin_type):
        amount = inquirer.text(message=f'How many {coin_type} do you have?:', validate =NumberValidator(message="Please type in a number.")).execute()
        return amount
    user_country = get_country()
    if user_country == 'United States':
        for country_value_dict in coin_value_list:
            if country_value_dict['country'] == 'US':
                US_dict = copy.deepcopy(country_value_dict)
                coin_type = 'Pennys'
        dollar_coin_amount = 0
        quarter_amount = 0
        dime_amount = 0
        nickel_amount = 0
        penny_amount = 0
        user_amount = (get_coin_amount(coin_type))
        while user_amount > 0 and user_amount != 0:
            if user_amount >= 100:
                user_amount -= US_dict['dollar_coin']
                dollar_coin_amount += 1
            elif user_amount <= 99 and user_amount >= 25:
                user_amount -= US_dict['quarter']
                quarter_amount += 1
            elif user_amount <= 24 and user_amount >= 10:
                user_amount -= US_dict['dime']
                dime_amount += 1
            elif user_amount <= 9 and user_amount >= 5:
                user_amount -= US_dict['nickel']
                nickel_amount += 1
            elif user_amount <= 4:
                user_amount -= US_dict['penny']
                penny_amount += 1
        print(f'From your total amount {user_amount} there was:')
        print(f'{dollar_coin_amount} many dollar coins.')
        print(f'{quarter_amount} this many quarters.')
        print(f'{dime_amount} this many dimes.')
        print(f'{nickel_amount} this many nickels.')
        print(f'{penny_amount} this many pennys.')
    elif user_country == 'Europe':
        pass