import random
def get_lottery_numbers():
    num_list = []
    for x in range(6): # This will determine how many winning numbers you want in a lottery. 
        num = random.randint(1, 49)
        while num in num_list:
            num = random.randint(1, 49)
        num_list.append(num)
    return num_list

def get_lottery_winner(lottery_numbers):
    lottery_winner = []
    counter = 0
    while lottery_winner != lottery_numbers:
        counter += 1
        lottery_winner = get_lottery_numbers()
    return lottery_numbers, counter
        
def main():
    lottery_numbers = get_lottery_numbers()
    lottery_winner, counter = get_lottery_winner(lottery_numbers)
    print(f"""
Winner Found!
Official numbers: {sorted(lottery_numbers)}
Ticket: {sorted(lottery_winner)}, Ticket #: {counter}""")
main()
