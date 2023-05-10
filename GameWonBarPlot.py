import matplotlib.pyplot as plt
import pdb

# Read data from a text file
with open('/Users/ualguest/Desktop/INFO 550 - AI - TM/Final Project/Game Won - Bar Plot Data.txt', 'r') as file:
    data = file.read().strip()

# Split the data by commas and remove any leading/trailing spaces
results = [result.strip() for result in data.split(',')]

# Count wins and losses
wins = results.count('Win')
losses = results.count('Loss')
total = wins + losses


# Plotting the bar graph
labels = ['Total','Wins', 'Losses']
values = [total, wins, losses]

# Extend the y-axis range
y_max = total
y_ticks = [100 * i for i in range((y_max // 100) + 2)]


#pdb.set_trace()
plt.bar(labels, values)
plt.xlabel('Game Result')
plt.ylabel('Number of Wins/Loss')
plt.title('Training Model Win-Loss Record')
plt.yticks(y_ticks)

# Display count on top of each bar
for i, value in enumerate(values):
    plt.text(i, value + 10, str(value), ha='center')
    
plt.show()

