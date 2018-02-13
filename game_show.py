prize_list = ['a','b','c','d','e','f','g','h','i']
while True:
    try:
        user_pick = int(input('select a number 1 through 10: '))

    except:
        print('numbers only please')

    try:
        print(prize_list[user_pick - 1])
    except:
        print('numbers 1 through 10 only please')
