#"""
#1. create a webscraper that grabs the latest baseball scores from yahoo for each team
#2. Create a canvas that holds a team selector that contains each team
#3. when a team is selected, display the latest score on the canvas below the team selector
#"""

import tkinter as tk
import pyautogui as pg
import time
import requests
import re
import sys
from bs4 import BeautifulSoup

# store team name and team code
team_names = {"Atlanta":"atl", "Arizona":"ari", "Baltimore":"bal", "Boston":"bos", "Chi Cubs":"chc", "Chi White Sox":"cws", "Cincinnati":"cin", "Cleveland":"cle", "Colorado":"col", "Detroit":"det", "Houston":"hou", "Kansas City":"kc", "LA Angels":"laa", "LA Dodgers":"lad", "Miami":"mia", "Milwaukee":"mil", "Minnesota":"min", "NY Mets":"nym", "NY Yankees":"nyy", "Oakland":"oak", "Philadelphia":"phi", "Pittsburgh":"pit", "San Diego":"sd", "San Francisco":"sf", "Seattle":"sea", "St. Louis":"stl", "Tampa Bay":"tb", "Texas":"tex", "Toronto":"tor", "Washington":"was"}
team_codes = {"Atlanta":"atl", "Arizona":"ari", "Baltimore":"bal", "Boston":"bos", "Chi Cubs":"chc", "Chi White Sox":"cws", "Cincinnati":"cin", "Cleveland":"cle", "Colorado":"col", "Detroit":"det", "Houston":"hou", "Kansas City":"kc", "LA Angels":"laa", "LA Dodgers":"lad", "Miami":"mia", "Milwaukee":"mil", "Minnesota":"min", "NY Mets":"nym", "NY Yankees":"nyy", "Oakland":"oak", "Philadelphia":"phi", "Pittsburgh":"pit", "San Diego":"sd", "San Francisco":"sf", "Seattle":"sea", "St. Louis":"stl", "Tampa Bay":"tb", "Texas":"tex", "Toronto":"tor", "Washington":"was"}

def get_score(team_name):
    team_code = team_codes[team_name]
    url = "http://sports.yahoo.com/mlb/teams/" + team_code + "/stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', {"class":"statistics"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        print(cols)

def get_scores():
    for team_name in team_codes:
        team_code = team_codes[team_name]
        url = "http://sports.yahoo.com/mlb/teams/" + team_code + "/stats"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('table', {"class":"statistics"})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            print(cols)

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def get_team_names():
    return team_names

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()