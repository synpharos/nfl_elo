# if game['result1'] == 0.5 (Ничья):
mult = math.log(max(pd, 1) + 1.0) * (2.2 / 1.0)

# if game['result1'] == 1.0 (Победа для Team 1):
mult = math.log(max(pd, 1) + 1.0) * (2.2 / (elo_diff * 0.001 + 2.2))

# if game['result1'] == 0.0 (Поражение для Team 1):
mult = math.log(max(pd, 1) + 1.0) * (2.2 / (-elo_diff * 0.001 + 2.2))
