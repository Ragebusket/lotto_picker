
import random

#list matched to dictionary
lotto_list = ['Powerball', 'Megabucks', 'MegaMillions', 'Lotto America', 'Lucky for Life', 'gimme 5', 'Pick 3', 'Pick 4']
# Lotto's name: 0. amount of numbers picked, 1. min range, 2. max range +1, 3. name of bonus number, 4. max range of bonus, 5. extra multiplier name
lotto_dic = {'Powerball': [ 5, 1, 70,'Powerball', 27, 'None'], 'Megabucks': [ 5, 1, 42,'Mega Number', 6, 'None'], 'MegaMillions': [ 5, 1, 71, 'Megaplier', 26, 'None'], 'Lotto America': [ 5, 1, 53, 'Star Ball',11, 'All Star Bonus'], 'Lucky for Life': [5, 1, 47, 'Lucky Ball', 19, 'None'], 'gimme 5': [5, 1, 40, 'None', 0, 'None'], 'Pick 3': [3, 0, 10, 'None', 0, 'None'], 'Pick 4': [4, 0, 10, 'None', 0, 'None']}


def non_number_bonus(which):
    #creates prompt to choose extra multiplier poption if aapplicable
    while True:
        want_extra = str(input('Enter "YES" or "NO" for bonus multiplier: '))
        try:
            if want_extra.lower() == 'no':
                return 'No'
            elif want_extra.lower() == 'yes':
                return 'Yes'
        except:
            print('Please enter YES or NO: ')

 
def main_numbers(runs, which):
    #creates list of primary lottery numbers
    for runs in range(lotto_dic[which][0]):
        lotto_numbers = []
        while len(lotto_numbers) < lotto_dic[which][0]:
            a_number = random.randrange(lotto_dic[which][1], lotto_dic[which][2])
            if a_number not in lotto_numbers:
                lotto_numbers.append(a_number)
            else:
                main_numbers(runs, which)
        lotto_numbers.sort()
        return lotto_numbers


def bonus_num_picker(which):
    #single bonus number chosen for applicable lotteries
    while True:
        try:
            return random.randrange(1, lotto_dic[which][4])
        except:
            return 'None'


def all_purpose_lottery_func(run_passes, which):
    #directs which series of functtions are needed for each lottery
    which = which
    bonus_num = 0
    for cycles in range(0, run_passes):
        b_num_position = lotto_list.index(which)
        numbers = main_numbers(run_passes, which)
        bonus_num = bonus_num_picker(which)
        bon_name = lotto_dic[which][3]
        if lotto_dic[which][5] != 'None':
            bonus_mult = non_number_bonus(which)
            print(*numbers, bon_name, ': ', bonus_num, ' Multiplier: ', bonus_mult)
        elif lotto_dic[which][3] != 'None':

            print(*numbers, bon_name, ': ', bonus_num)
        else:
            print(*numbers)


def run_it_all():
    #Initial prompt/inputs for each lottery
    place_holder = 0
    for lotto in lotto_dic:
        def choice_selects(lotto):
            runs = 0
            while True:
                try:
                    runs = input("How many " + lotto + " entries would you like to generate?: ")
                    runs = int(runs)
                    break
                except ValueError:
                    print("Please enter a valid number. Enter 0 to skip this lottery.")
            if runs == 0:
                print("No " + lotto_list[runs] + " number generated")
            else:
                print('Your ' + lotto + ' numbers are:')

                all_purpose_lottery_func(runs, lotto)
        choice_selects(lotto)

#run it
run_it_all()

