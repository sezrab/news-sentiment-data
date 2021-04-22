import matplotlib.pyplot as plt
import csv

# make graph
x = []
y = []

with open('csv/mean-sentiment.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

plt.plot(x, y, label="Mean daily sentiment")
plt.xlabel('Date')
plt.ylabel('Sentiment')
plt.legend()
if len(x) > 7:
    plt.xticks(range(0,len(x),len(x)//5))
plt.tight_layout()
plt.savefig('img/daily-sentiment-graph.png')