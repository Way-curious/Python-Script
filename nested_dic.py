allGuests = {'Alice': {'apples': 5, 'pretzels': 12, 'money': 23},
            'Bob': {'ham sandwiches': 3, 'apples': 2, 'money': 25},
            'Carol': {'cups': 3, 'apple pies': 1, 'money':30}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
print(' - Total revenue ' + str(totalBrought(allGuests, 'money')))