"""
Problem:
https://www.testdome.com/questions/python/league-table/94851
"""

from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        ranking = list()

        def custom_sort(item):
            player, standing = item
            games_played = standing["games_played"]
            score = standing["score"]
            return score * -1, games_played

        players_rank = sorted(self.standings.items(), key=custom_sort)

        for player, standing in players_rank:
            ranking.append(player)

        return ranking[rank - 1]


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))