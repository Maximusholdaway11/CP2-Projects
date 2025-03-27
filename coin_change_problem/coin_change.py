#Max Holdaway Coin Change Problem: Coin Change function(s)
import csv

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
                us_coin_values_dict = {'penny': penny_value, 'nickel': nickel_value, 'dime': dime_value, 'quarter': quarter_value, 'dollar_coin': dollar_value}
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
                eu_coin_values_dict = {'one_euro_cent': euro_cent_one_value, 'two_euro_cent': euro_cent_two_value, 'five_euro_cent': euro_cent_five_value, 'ten_euro_cent': euro_cent_ten_value, 'twenty_euro_cent': euro_cent_twenty_value, 'fifty_euro_cent': euro_cent_fifty_value, 'one_euro': euro_one_value, 'two_euros': euro_two_value}
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
                br_coin_values_dict = {'one_pence': pence_one_value, 'two_pence': pence_two_value, 'five_pence': pence_five_value, 'ten_pence': pence_ten_value, 'twenty_pence': pence_twenty_value, 'fifty_pence': pence_fifty_value, 'one_pound': pound_one_value, 'two_pounds': pound_two_value}
                coin_value_list.append(br_coin_values_dict)
            elif row[0] =='JP':
                one_yen_split = row[1].split('-')
                one_yen_value = {'coin_name': 'Penny', 'coin_value': float(penny_split[1])}
                five_yen_split = row[2].split('-')
                five_yen_value = {'coin_name': 'Nickel', 'coin_value': float(nickel_split[1])}
                ten_yen_split = row[3].split('-')
                ten_yen_value = {'coin_name': 'Dime', 'coin_value': float(dime_split[1])}
                fifty_yen_split = row[4].split('-')
                fifty_yen_value ={'coin_name': 'Quarter', 'coin_value': float(quarter_split[1])}
                hundred_yen_split = row[5].split('-')
                hundred_yen_value = {'coin_name': 'Dollar Coin', 'coin_value': float(dollar_split[1])}
                jp_coin_values_dict = {'penny': penny_value, 'nickel': nickel_value, 'dime': dime_value, 'quarter': quarter_value, 'dollar_coin': dollar_value}
                coin_value_list.append(jp_coin_values_dict)