import requests
import json
from textblob import TextBlob
from bs4 import BeautifulSoup
import csv
from datetime import date
import os

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
headers = {"User-Agent": ua}

# todo: telegraph, economist, financial times, daily mirror


def getSoup(url):
    response = requests.get(url, headers=headers).content
    return BeautifulSoup(response, features="html.parser")


def bbc():
    soup = getSoup("https://www.bbc.co.uk/news")
    storyHeadings = soup.find_all("h3", {"class": "gs-c-promo-heading__title"})
    headingTexts = [
        heading.text for heading in storyHeadings if heading.text != ""]
    return headingTexts


def sky():
    soup = getSoup("https://news.sky.com/")
    storyHeadings = soup.find_all(
        "span", {"class": "sdc-site-tile__headline-text"})
    headingTexts = [
        heading.text for heading in storyHeadings if heading.text != ""]
    return headingTexts


def reuters():
    soup = getSoup("https://www.reuters.com/")
    storyHeadings = soup.find_all(
        "span", {"class": "MediaStoryCard__title___2PHMeX"})
    headingTexts = [
        heading.text for heading in storyHeadings if heading.text != ""]
    return headingTexts


def reddit(url):
    jsonResponse = requests.get(url, headers=headers).content
    jsonData = json.loads(jsonResponse)
    titles = [post["data"]["title"] for post in jsonData["data"]["children"]]
    return titles


sites = ["BBC News", "Sky", "Reuters",
         "r/worldnews", "r/news"]  # for csv headers


def main():
    news = [bbc(), sky(), reuters(), reddit(
        "https://www.reddit.com/r/worldnews/hot.json"), "https://www.reddit.com/r/news/hot.json"]

    means = []

    for site in news:
        total = 0
        for title in site:
            total += TextBlob(title).sentiment.polarity
        means.append(total/len(site))


    meanSentiment = sum(means)/len(means)
    today = date.today().strftime("%d/%m/%Y")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path+'/csv/mean-sentiment.csv', 'r+', newline="") as csvfile:
        if today not in csvfile.read():
            print("Writing mean sentiment")
            writer = csv.writer(csvfile)
            writer.writerow([today, meanSentiment])

    with open(dir_path+'/csv/site-mean-sentiment.csv', 'r+', newline="") as csvfile:
        if today not in csvfile.read():
            print("Writing per site mean sentiment")
            rows = [[today]+row for row in csv.reader(csvfile, delimiter=',')][1:]
            csvfile.seek(0)
            csvfile.truncate()
            writer = csv.writer(csvfile)
            writer.writerow(["date"]+sites)
            writer.writerows(rows)
            writer.writerow([today]+means)