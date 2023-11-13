import random
count = 100
double = 0
while count>0:
    i = random.randint(1,6)
    j = random.randint(1,6)
    if i == j :
        double = double +1
    count = count - 1

print('Out of 100 you rolled',double,"doubles" )
    
