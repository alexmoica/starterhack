#[Assignment Name, Mark, Weight]
listlist = [['Assignment1', 0.95, 2], ['Assignment2', 0.84, 2], ['Lab1', 0.64, 5], ['Lab2', 0.90, 5], ['Midterm', 0.81, 20], ['Quiz1', 1, 1], ['Quiz2', .9, 1]]

AssTotalWeight = 0
AssCurrentWeight = 0
LabTotalWeight = 0
LabCurrentWeight = 0
MidTotalWeight = 0
MidCurrentWeight = 0
QuizTotalWeight = 0
QuizCurrentWeight = 0

#Determines the which group the marks are assigned to (whether it be in the assignment section or the quiz section)

for i in listlist:
    if i[0][:3] == 'Ass' or "ASS":
        AssTotalWeight += i[2]
        AssCurrentWeight += (i[1] * i[2])
        
    elif i[0][:3] == 'Lab' or "LAB":
        LabTotalWeight += i[2]
        LabCurrentWeight += (i[1] * i[2])
    elif i[0][:3] == 'Mid' or "MID":
        MidTotalWeight += i[2]
        MidCurrentWeight += (i[1] * i[2])
    elif i[0][:4] == 'Quiz' or "QUIZ":
    	QuizTotalWeight += i[2]
    	QuizCurrentWeight += (i[1] * i[2])
    else:
    	pass


#print(AssCurrentWeight/AssTotalWeight, LabCurrentWeight/LabTotalWeight)

#Calculates the total amount of marks received & what is left 

Total_Weight = AssTotalWeight + LabTotalWeight + QuizTotalWeight + MidTotalWeight 
Current_Weight = AssCurrentWeight + LabCurrentWeight + QuizCurrentWeight + MidCurrentWeight
Remaining_Weight = 100-Total_Weight


Current_Mark = (Current_Weight/Total_Weight)*100

print("Your current mark is",round(Current_Mark, 1), "%")

while True:
    try:
        x = float(input("What final grade do you want? (Do not include '%')"))
        break
    except ValueError:
        print("Please print a percentage (no '%' symbol")


Weight_Needed = x - Current_Weight
Percentage_Needed = round(100*(Weight_Needed/Remaining_Weight), 1)
    

print("You need a", Percentage_Needed, "%",'in the rest of the course to obtain a', x, '%', 'average')
