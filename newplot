import matplotlib.pyplot as plt

def make_picker(fig, wedges):

    def onclick(event):
        wedge = event.artist
        label = wedge.get_label()
        print (label)

# Make wedges selectable
    for wedge in wedges:
        wedge.set_picker(True)

    fig.canvas.mpl_connect('pick_event', onclick)

# Make an example pie plot

fig = plt.figure()
ax = fig.add_subplot(111)

labels1 = ['1ZA3', '1D03', '1E03', '1ZC3', '1D04', '2CI5']
weight = []

for i in labels:
    x = int(i[(len(i)-1):])
    weight.append(x)
    
ax.pie(weight, labels=labels1, autopct= '%1.2f%%', shadow=True)

wedges, plt_labels = ax.pie(weight, labels=labels)
ax.axis('equal')

make_picker(fig, wedges)

plt.show()
