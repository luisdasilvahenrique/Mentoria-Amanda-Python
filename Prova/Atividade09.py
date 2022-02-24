myList=[-5,10,7,5,-6,8,5,-15]

for index, value in enumerate(myList):
    if value < 0:
        myList[index] = 0

print(myList)