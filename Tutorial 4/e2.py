total = 0 # sum of scores
count = 0 # number of scores entered

# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): ") )

    
# Add while loop here. Loop while score is not -9
while (score != '-9') :
    total = total + int(score)
    count = count +1
    score = input("Enter score, (Enter -9 to end): ")
# Add score to total
# Keep a count of scores
# Get next score input

# print average of scores entered
average = float( total ) / count
print("Class average is", average)
