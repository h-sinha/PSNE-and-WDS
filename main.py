import numpy as np
import sys
import time

def read_input():
	try:
		num_players = int(input())
		num_strategy = np.array(list(map(int,input().strip().split())))
		payoffs = np.array(list(map(int,input().strip().split())))
		n_size = num_strategy
		n_size = np.append(n_size, num_players)
		payoffs.resize(n_size)
		# payoffs X,i,j,k,.... = payoff for player X for s1i, s2j, s3k,....
		payoffs = np.transpose(payoffs)
		return num_players, num_strategy, payoffs
	except:
		print("Incorrect input")
		sys.exit()

start = time.time()
num_players, num_strategy, payoffs = read_input()
end = time.time()
print(end-start)

PSNE = []
best_utility = np.array(payoffs)

def check_PSNE(strategies):
	for i in range(num_players):
		if best_utility[i][tuple(strategies)] > payoffs[i][tuple(strategies)]:
			return
	PSNE.append(np.array(strategies))
def find_PSNE(player, strategies):
	if player == num_players:
		check_PSNE(strategies)
		return
	for i in range(num_strategy[player]):
		strategies.append(i)
		find_PSNE(player + 1, strategies)
		strategies.pop()
def compute_best_utility(cur_player, player, left_index, right_index):
	if cur_player == num_players :
		max_value = payoffs[player][tuple(left_index)][0][tuple(right_index)]
		for i in range(num_strategy[player]):
			if len(left_index) == 0:
				max_value = max(max_value, payoffs[player][i][tuple(right_index)])
			elif len(right_index) == 0:
				max_value = max(max_value, payoffs[player][tuple(left_index)][i])
			else:
				max_value = max(max_value, payoffs[player][tuple(left_index)][i][tuple(right_index)])
		for i in range(num_strategy[player]):
			if len(left_index) == 0:
				best_utility[player][i][tuple(right_index)] = max_value
			elif len(right_index) == 0:
				best_utility[player][tuple(left_index)][i] = max_value
			else:
				best_utility[player][tuple(left_index)][i][tuple(right_index)] = max_value
		return
	if player == cur_player:
		compute_best_utility(cur_player + 1, player, left_index, right_index)
	else:
		for i in range(num_strategy[cur_player]):
			if cur_player < player:
				left_index.append(i)
				compute_best_utility(cur_player + 1, player, left_index, right_index)
				left_index.pop()
			else:
				right_index.append(i)
				compute_best_utility(cur_player + 1, player, left_index, right_index)
				right_index.pop()
start = time.time()
for i in range(num_players):
	compute_best_utility(0, i, [], [])
end = time.time()
print(end-start)

start = time.time()
find_PSNE(0, [])
end = time.time()
print(end-start)


start = time.time()

# printing PSNE
print(len(PSNE))
for v in PSNE:
	for x in v: 
		print(x+1, end = " ")
	print("")
end = time.time()
print(end-start)
