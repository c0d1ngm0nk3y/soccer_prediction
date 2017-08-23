from prediction.Oracle import Oracle

oracle = Oracle()
games = oracle.predict_game_day('bl1', '2016', 33)

for game in games:
    game.print_it()