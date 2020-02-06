import sys
import os
import unittest
from mamba import *
from expects import *

from hashketball import *

def players():
    return {
    'Alan Anderson': {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1}, 'Reggie Evans': {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7}, 'Brook Lopez': {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15}, 'Mason Plumlee': {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 11, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5}, 'Jason Terry': {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}, 'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2}, 'Bismack Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 22, 'blocks': 15, 'slam_dunks': 10}, 'DeSagna Diop': {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5}, 'Ben Gordon': {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0}, 'Kemba Walker': {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 7, 'blocks': 5, 'slam_dunks': 12}
}

class TestSum(unittest.TestCase):

    def test_game_dict_is_dictionary(self):
        self.assertEqual(type(game_dict()), dict, 'Method game_dict should return a dictionary')

    def test_game_dict_has_team_keys(self):
        team_keys = ['away', 'home']
        self.assertEqual(all(item in team_keys for item in game_dict().keys()), True, '''game_dict should have 'away' and 'home' as keys''')

    def test_game_dict_has_inner_keys(self):
        team_keys = ['team_name', 'colors', 'players']
        for key in game_dict().keys():
            nestedKeys = list(game_dict()[key].keys())
            self.assertEqual(all(item in team_keys for item in nestedKeys), True, """Each team in game_dict should include the nested keys of 'team_name', 'colors', and 'players'""")

    def test_num_points_scored(self):
        for name in players().keys():
            user_input = num_points_scored(name)
            points = players()[name]['points']
            self.assertEqual(points == user_input, True, "Should return the player's points for %s, which should equal -> %s. \nInstead got -> %s"%(name, points, user_input))

    def test_shoe_size(self):
        for name in players().keys():
            user_input = shoe_size(name)
            shoe = players()[name]['shoe']
            self.assertEqual(user_input == shoe, True, "Should return the player's shoe size for %s, which should equal -> %s. \nInstead got -> %s"%(name, shoe, user_input))

    def test_team_colors(self):
        teams = { 
            "Brooklyn Nets": ['Black', 'White'],
            "Charlotte Hornets": ["Turquoise", "Purple"]
        }
        for name in teams.keys():
            self.assertEqual(all(item in teams[name] for item in team_colors(name)) and len(teams[name]) == len(team_colors(name)), True, "Should display the proper team colors for the team %s which is %s. Instead got -> %s."%(name, teams[name], team_colors(name)))
    
    def test_team_names(self):
        names = ["Brooklyn Nets", "Charlotte Hornets"]
        self.assertEqual(all(item in names for item in team_names()) and len(names) == len(team_names()), True, 'Should return an array of all the team names -> %s'%(names))

    def test_player_numbers(self):
        teams = { 
            "Brooklyn Nets": [0, 1, 11, 30, 31],
            "Charlotte Hornets": [0, 2, 4, 8, 33]
        }
        for key in teams.keys():
            userInput = player_numbers(key)
            self.assertEqual(all(item in teams[key] for item in userInput) and len(teams[key]) == len(userInput), True, 'Should return an array of all the player numbers for the %s -> %s. Instead got -> %s.'%(key, teams[key], userInput))

    def test_players_stats(self):
        for name in players().keys():
            userInput = player_stats(name)
            stats = players()[name]
            self.assertEqual(stats == userInput, True, "Should return a dictionary with all the players stats when given a player's name. %s -> should return -> %s. \nInstead got -> %s"%(name, stats, userInput))

    

expect(type([])).to(equal(list))
expect([]).to(be_empty)

expect(False).not_to(be_true)

expect({
    'name': 'Jack',
    'email': 'jack@example.com'
}).to(have_key('name', match('\w+')))

expect(str).to(have_property('split') & be_callable)

expect(lambda: foo).to(raise_error(NameError))

expect('Foo').to(equal('Bar') | equal('Foo'))

if __name__ == '__main__':
    unittest.main()