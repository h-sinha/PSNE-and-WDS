import numpy as np
import sys
import time

def get_payoff(payoffs, player, offset, num_strategy):
	l =  np.array([payoffs[x] for x in range(player, len(payoffs), offset)])
	l = l.reshape(num_strategy)
	return np.transpose(l)
def read_input():
	try:
		input = sys.stdin.readline
		num_players = int(input())
		num_strategy = np.array(list(map(int,input().strip().split())))
		temp_payoffs = np.array(list(map(int,input().strip().split())))
		n_size = np.append(num_players, num_strategy)
		# payoffs X,i,j,k,.... = payoff for player X for s1i, s2j, s3k,....
		payoffs = np.zeros(n_size)
		num_strategy = num_strategy[::-1]
		for i in range(num_players):
			payoffs[i] = get_payoff(temp_payoffs, i, num_players, num_strategy)
		num_strategy = num_strategy[::-1]
		return num_players, num_strategy, payoffs
	except:
		print("Incorrect input")
		sys.exit()

num_players, num_strategy, payoffs = read_input()
is_WDS = [set() for _ in range(num_players)]
for i in range(num_players):
	for x in range(num_strategy[i]):
		is_WDS[i].add(x)

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
		# for WDS
		for i in range(num_strategy[player]):
			cur_util = 0
			if len(left_index) == 0:
				cur_util = payoffs[player][i][tuple(right_index)]
			elif len(right_index) == 0:
				cur_util = payoffs[player][tuple(left_index)][i]
			else:
				cur_util = payoffs[player][tuple(left_index)][i][tuple(right_index)]
			if cur_util < max_value:
				is_WDS[player].discard(i)
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
for i in range(num_players):
	compute_best_utility(0, i, [], [])
find_PSNE(0, [])

# printing PSNE
sys.stdout.write(str(len(PSNE)) + "\n")

for v in PSNE:
	sys.stdout.write(" ".join(str(x+1) for x in v))
	sys.stdout.write("\n")

# WDS
for i in range(num_players):
	if len(is_WDS[i]) > 1:
		sys.stdout.write("0" + "\n")
		continue
	sys.stdout.write(str(len(is_WDS[i])) + " ")
	sys.stdout.write(" ".join(str(x+1) for x in is_WDS[i]))
	sys.stdout.write("\n")
