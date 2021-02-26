import numpy as np

def read_input():
	num_players = int(input())
	num_strategy = np.array(list(map(int,input().strip().split())))
	payoffs = np.array(list(map(int,input().strip().split())))
	n_size = num_strategy
	n_size = np.append(n_size, num_players)
	# payoffs i,j,k,.....,X = payoff for player X for s1i, s2j, s3k,....
	payoffs.resize(n_size)
	return num_players, num_strategy, payoffs

if __name__ == '__main__':
	read_input()
	# num_players, num_strategy, payoffs = read_input()