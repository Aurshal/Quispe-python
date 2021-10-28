import random

t_user_score = 0
t_comp_score = 0

comp_die1 = 0
comp_die2 = 0


def conclude():
    if((t_user_score) > (t_comp_score)):
        print('\nYou beat the computer!')
    if((t_user_score) < (t_comp_score)):
        print('\nThe computer won.\nBetter luck next time.')
    else:
        print('\nGood job!')


def scoreRoll(die1, die2):
    if(die1+die2 == 3):
        score = 1000
    elif(die1 == die2):
        score = die1 * 100
    else:
        score = die1 * 10 + die2
    return score


def u_sum(num):
    global t_user_score
    t_user_score =  t_user_score + num
    return t_user_score


def c_sum(num):
    global t_comp_score
    t_comp_score += num
    return t_comp_score


def choose_selection2():
    print('\nChoose one of the following options:')
    print('1.  Continue Playing')
    print('2.  Stop Playing')
    selection2 = int(input('Selection:  '))
    return(selection2)


def reroll(die1, die2):
    user_die1 = die1
    user_die2 = die2

    print('\nChoose one of the following selections')
    print('1.  Reroll your first die')
    print('2.  Reroll your second die')
    print('3.  Keep your original roll')
    selection1 = int(input('Enter selection:  '))

    if(selection1 == 1):
        t_user_score = 0
        t_computer_score = 0
        user_die1 = random.randint(1, 6)
        user_score = scoreRoll(user_die1, user_die2)
        comp_score = scoreRoll(comp_die1, comp_die2)
        return user_die1, user_die2, user_score


    elif(selection1 == 2):

        t_user_score = 0
        t_computer_score = 0
        user_die2 = random.randint(1, 6)
        user_score = scoreRoll(user_die1, user_die2)
        comp_score = scoreRoll(comp_die1, comp_die2)
        return user_die1,user_die2,user_score

    elif(selection1 == 3):
        user_score = scoreRoll(user_die1, user_die2)
        comp_score = scoreRoll(comp_die1, comp_die2)
        return user_die1, user_die2, user_score


def display_total_score(user_die1,user_die2,comp_die1,comp_die2,user_score,comp_score):
    print()
    print('The final scores:')
    print('You rolled: ', user_die1, user_die2)
    print('Your score: ', user_score)
    print()
    print('Computer rolled: ', comp_die1, comp_die2)
    print('Computer score: ', comp_score)
    print()
    print('Total user score:\t', u_sum(user_score))
    print('Total computer score:\t', c_sum(comp_score))


def init():
    user_die1 = random.randint(1, 6)
    user_die2 = random.randint(1, 6)
    global comp_die1
    comp_die1 = random.randint(1, 6)
    global comp_die2
    comp_die2 = random.randint(1, 6)

    print('\nYou rolled: ', user_die1,user_die2)
    user_score = scoreRoll(user_die1, user_die2)
    print('Your score: ', user_score)

    print()

    print('Computer rolled: ', comp_die1,comp_die2)
    comp_score = scoreRoll(comp_die1, comp_die2)
    print('Computer score: ',  comp_score)

    user_die1,user_die2,user_score = reroll(user_die1, user_die2)
    display_total_score(user_die1, user_die2, comp_die1,
                        comp_die2, user_score, comp_score)
    if(choose_selection2() == 1):
            init()
    else:
        conclude()


def main():
    seed = int(input("Enter an integer to seed the random number generator:  "))
    random.seed(seed)
    init()
    

if __name__ == "__main__":
    main()
