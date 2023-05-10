import matplotlib.pyplot as plt

# Read scores from a text file
with open('/Users/ualguest/Desktop/INFO 550 - AI - TM/Final Project/Pacman Scores - Line Plot Data.txt', 'r') as file:
    data = [float(value) for value in file.read().split(',')]

# Create a line plot
average_values = []
for i in range(100, len(data) + 1, 100):
    chunk = data[:i]
    average = sum(chunk) / len(chunk)
    average_values.append(average)

# Create line plot
x_values = range(100, len(data) + 1, 100)
plt.plot(x_values, average_values, color='red')
plt.xlabel('Number of Trainings')
plt.ylabel('Average Scores')
plt.title('Average Scores')
plt.show()
