with open('input.txt', 'r') as f:
	read = lambda: [int(x) for x in f.readline().split()]
	line = read()
	players = {x:0 for x in range(int(line[0]))}
	for _ in range(int(line[1])):
		line = read()
		goals_A, goals_B = int(line[0]), int(line[1])
		line = read()
		for player in line[:5]: players[player] += goals_A - goals_B
		for player in line[5:]: players[player] += goals_B - goals_A
		print(len([player for player in players if players[player] > players[0]]))
