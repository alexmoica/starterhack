#MainPage Pie Chart
labels = ['1ZA3', '1D03', '1E03', '1ZC3', '1D04', '2CI5']
weight = []

#Takes the last number in the course code representing the credit/weight of the course
#Turns it into an integer and places it into a list that will be used to show the weight of the course relative to
#everything else

for i in labels:
    x = int(i[(len(i)-1):])
    weight.append(x)

#Establishes a figure and axis    
fig, ax, = plt.pyplot.subplots()
ax.pie(weight, labels = labels, autopct='%1.2f%%', shadow=True, startangle=0)

#makes sure that everything is equal spacing based on the numbers present
ax.axis('equal')

ax.set_title("Course Weight Towards the Semester's Average")


plt.pyplot.show()
