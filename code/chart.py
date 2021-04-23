import matplotlib.pyplot as plt
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

def plotMeanSentiment():
    x = []
    y = []
    with open(dir_path+'/csv/mean-sentiment.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(row[0])
            y.append(float(row[1]))

    plt.clf()
    plt.plot(x, y, label="Mean daily sentiment")
    plt.xlabel('Date')
    plt.ylabel('Sentiment')
    plt.legend()
    if len(x) > 7:
        plt.xticks(range(0, len(x), len(x)//5))
    plt.tight_layout()
    plt.savefig(dir_path+'/img/daily-sentiment-graph.png')

def plotPerSiteSentiment():
    plt.clf()
    with open(dir_path+'/csv/site-mean-sentiment.csv', 'r') as csvfile:
        plots = list(csv.reader(csvfile, delimiter=','))
        headers=plots[0]
        for i in range(2,len(headers)+1):
            x = []
            y = []
            for row in plots[1:]:
                x.append(row[0])
                y.append(float(row[i-1]))
            plt.plot(x, y, label=headers[i-1])
            plt.legend()

    plt.xlabel('Date')
    plt.ylabel('Sentiment')
    if len(x) > 7:
        plt.xticks(range(0, len(x), len(x)//5))
    plt.tight_layout()
    plt.savefig(dir_path+'/img/daily-site-sentiment-graph.png')

def main():
    plotMeanSentiment()
    plotPerSiteSentiment()

plotPerSiteSentiment()