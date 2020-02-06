import pry

def game_dict():
    return {
        'away': {
            'team_name': 'Charlotte Hornets',
            'colors': ['Turquoise', 'Purple'],
            'players': [
                {
                    'player_name': 'Jeff Adrien',
                    'number': 4,
                    'shoe': 18,
                    'points': 10,
                    'rebounds': 1,
                    'assists': 1,
                    'steals': 2,
                    'blocks': 7,
                    'slam_dunks': 2
                },
                { 'player_name': 'Bismack Biyombo',
                    'number': 0,
                    'shoe': 16,
                    'points': 12,
                    'rebounds': 4,
                    'assists': 7,
                    'steals': 22,
                    'blocks': 15,
                    'slam_dunks': 10 },
                { 'player_name': 'DeSagna Diop',
                    'number': 2,
                    'shoe': 14,
                    'points': 24,
                    'rebounds': 12,
                    'assists': 12,
                    'steals': 4,
                    'blocks': 5,
                    'slam_dunks': 5 },
                { 'player_name': 'Ben Gordon',
                    'number': 8,
                    'shoe': 15,
                    'points': 33,
                    'rebounds': 3,
                    'assists': 2,
                    'steals': 1,
                    'blocks': 1,
                    'slam_dunks': 0 },
                { 'player_name': 'Kemba Walker',
                    'number': 33,
                    'shoe': 15,
                    'points': 6,
                    'rebounds': 12,
                    'assists': 12,
                    'steals': 7,
                    'blocks': 5,
                    'slam_dunks': 12 }
                ] },
        'home': { 'team_name': 'Brooklyn Nets',
                'colors': ['Black', 'White'],
                'players': [
                { 'player_name': 'Alan Anderson',
                    'number': 0,
                    'shoe': 16,
                    'points': 22,
                    'rebounds': 12,
                    'assists': 12,
                    'steals': 3,
                    'blocks': 1,
                    'slam_dunks': 1 },
                { 'player_name': 'Reggie Evans',
                    'number': 30,
                    'shoe': 14,
                    'points': 12,
                    'rebounds': 12,
                    'assists': 12,
                    'steals': 12,
                    'blocks': 12,
                    'slam_dunks': 7 },
                { 'player_name': 'Brook Lopez',
                    'number': 11,
                    'shoe': 17,
                    'points': 17,
                    'rebounds': 19,
                    'assists': 10,
                    'steals': 3,
                    'blocks': 1,
                    'slam_dunks': 15 },
                { 'player_name': 'Mason Plumlee',
                    'number': 1,
                    'shoe': 19,
                    'points': 26,
                    'rebounds': 11,
                    'assists': 6,
                    'steals': 3,
                    'blocks': 8,
                    'slam_dunks': 5 },
                { 'player_name': 'Jason Terry',
                    'number': 31,
                    'shoe': 15,
                    'points': 19,
                    'rebounds': 2,
                    'assists': 2,
                    'steals': 4,
                    'blocks': 11,
                    'slam_dunks': 1 }
                ] }
    }

def all_players():
    players = game_dict()['home']['players'] + game_dict()['away']['players']
    allPlayers = list(map(set_player_name, players))
    players = dict()
    for player in allPlayers:
        players.update(player)
    return players

def set_player_name(player):
    name = [player['player_name']]
    del player['player_name']
    newPlayer = { name[0]: player }
    return newPlayer

def num_points_scored(player):
    return all_players()[player]['points']

def shoe_size(player):
    return all_players()[player]['shoe']

def team_colors(team):
    if game_dict()['home']['team_name'] == team:
        return game_dict()['home']['colors']
    else:
        return game_dict()['away']['colors']

def team_names():
    return [game_dict()['home']['team_name'],game_dict()['away']['team_name']]

def player_numbers(team):
    if game_dict()['home']['team_name'] == team:
        return list(map(getNumbers, game_dict()['home']['players']))
    else:
        return list(map(getNumbers, game_dict()['away']['players']))

def getNumbers(player):
    return player['number']

def player_stats(player):
    return all_players()[player]

