#Max Holdaway Coin Change Problem: Coin Change function(s)
import csv

def load_coin_values(coin_value_list):
    with open("coin_change_problem/coin_values.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == 'US':
                penny_split = row[1].split('-')
                penny_value = {'coin_name': penny_split[0], 'coin_value': int(penny_split[1])}
                nickel_split = row[2].split('-')
                nickel_value = {'coin_name': nickel_split[0], 'coin_value': int(nickel_split[1])}
                dime_split = row[3].split('-')
                dime_value = {'coin_name': dime_split[0], 'coin_value': int(dime_split[1])}
                quarter_split = row[4].split('-')
                quarter_value ={'coin_name': quarter_split[0], 'coin_value': int(quarter_split[1])}
                dollar_split = row[5].split('-')
                dollar_value = {'coin_name': dollar_split[0], 'coin_value': int(dollar_split[1])}
                us_coin_values_dict = {'penny': penny_value, 'nickel': nickel_value, 'dime': dime_value, 'quarter': quarter_value, 'dollar_coin': dollar_value}
                coin_value_list.append(us_coin_values_dict)