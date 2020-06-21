print('welcome to Hotel CrossRoads')
print('please select your dishes from the list')
rice = ['1. White Rice', '2. Plain Rice', '3. Biriyani', '4. Fried Rice', '5. Mandi']
drinks = ['1. Mineral water', '2. Orange Juice', '3. Apple Juice', '4. none']
for x in rice:
    print(x)
riceSelection = int(input('press the number to select the dish'))
if riceSelection == 1:
    order = [(rice[0])]
elif riceSelection == 2:
    order = [(rice[1])]
elif riceSelection == 3:
    order = [(rice[2])]
elif riceSelection == 4:
    order = [(rice[3])]
elif riceSelection == 5:
    order = [(rice[4])]
else:
    order = ['invalid selection']

for x in drinks:
    print(x)
drinksSelection = int(input('Please Select the Drinks'))

if drinksSelection == 1:
    order.append(drinks[0])
elif drinksSelection == 2:
    order.append(drinks[1])
elif drinksSelection == 3:
    order.append(drinks[2])
elif drinksSelection == 4:
    order.append('you have not selected any drink')
else:
    order.append('invalid selection')

print('your orders are')
for x in order:
    print(x)
    print("and")
print('thank you for dining here, please wait untill your order is prepared')
print('have a nice day')
