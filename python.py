file = open("day2.txt","r")
pointTotal1 = 0
pointTotal2 = 0

matchOutcomes = {
    "A X":4, "B X":1, "C X": 7,
    "A Y":8, "B Y":5, "C Y": 2,
    "A Z":3, "B Z":9, "C Z": 6
}

matchOutcomes2 = {
    "A X":3, "B X":1, "C X": 2,
    "A Y":4, "B Y":5, "C Y": 6,
    "A Z":8, "B Z":9, "C Z": 7
}

for line in file:  
    pointTotal1 += matchOutcomes[line[0:3]]
    pointTotal2 += matchOutcomes2[line[0:3]]
    
print(pointTotal1)  
print(pointTotal2)