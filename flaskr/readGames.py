from flaskr.analyze_baseball import calcNTeamSeasonResult
from flaskr.model import Input, SeasonResult

import os

def readGames(teamOF, opps, years):
    os.chdir('flaskr/static')
    seasons = []
    for file in os.listdir():
        file_path = file
        l = len(file_path)
        year = file_path[l-8:l-4]
        yearRange = range(int(years[0]), int(years[1]), 1) 
        count = yearRange.count(int(year))
        if (count > 0):
            seasonResult = calcNTeamSeasonResult(file_path, Input(year, teamOF, opps))
            seasons.append(seasonResult.toJson())
    os.chdir('../..')
    return seasons