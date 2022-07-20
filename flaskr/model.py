import json

class Input:
    def __init__(self, year, teamOFName, opps):
        self.year = year
        self.teamOFName = teamOFName
        self.opps = opps

class SeasonResult:
    def __init__(self, year, focusTeam, opponents, gamesPlayed, winPercents):
        self.year = year
        self.focusTeam = focusTeam
        self.opponents = opponents
        self.gamesPlayed = gamesPlayed
        self.winPercents = winPercents

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Team:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.winCount = 0
        self.gamesPlayed = 0

class Game:
    def __init__(self, input, home, away):
        self.input = input
        self.home = home
        self.away = away