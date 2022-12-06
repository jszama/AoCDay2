file = open("day2.txt","r")
pointTotal = 0

matchOutcomes = {
    "A X":4, "B X":1, "C X": 7,
    "A Y":8, "B Y":5, "C Y": 2,
    "A Z":3, "B Z":9, "C Z": 6
}

for line in file:  
    print(line[0:3].strip("\n"))
    pointTotal += matchOutcomes[line[0:3].strip("\n")]
    
print(pointTotal)