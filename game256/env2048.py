import numpy as np
import sys
import math
import random
from six import StringIO, b

from gym import utils
from gym.envs.toy_text import discrete

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game2048Env(discrete.DiscreteEnv):
	"""
	OpenAI gym environment for popular game 2048
	Goal: to reach 2048 by moving tiles
	"""
	
	def __init__(self, is_slippery=True):
		matrix = [ 0 for i in range(16) ]
		rand_lst = random.sample( range(16), 2)
		matrix[rand_lst[0]] = matrix[rand_lst[1]] = 2
		self.nrow, self.ncol = nrow, ncol = 4,4
		self.matrix = matrix
		global score
		score = 0

	def move(matrix, direction):
		new = list(matrix)
		merged = []
		global score
		if direction == 0:
			for i in range(15, 3, -1):
				if new[i] == 0:
					continue
				if new[i-4] == 0:
					new[i-4] = new[i]
					new[i] = 0
				elif new[i-4] == new[i] and i-4 not in merged and i not in merged:
					new[i-4] *= 2
					score = score + new[i-4]
					new[i] = 0
					merged.append(i-4)
		elif direction == 1:
			for i in range(16):
				if new[i] == 0:
					continue
				if i%4 != 3:
					if new[i+1] == 0:
						new[i+1] = new[i]
						new[i] = 0
					elif new[i+1] == new[i] and i not in merged:
						new[i+1] *= 2
						new[i] = 0;
						score = score + new[i+1]
						merged.append(i+1)
		elif direction == 2:
			for i in range(12):
				if new[i] == 0:
					continue
				if new[i+4] == 0:
					new[i+4] = new[i]
					new[i] = 0
				elif new[i+4] == new[i] and i not in merged:
					new[i+4] *= 2
					new[i] = 0
					score = score + new[i+4]
					merged.append(i+4)
		elif direction == 3:
			for i in range(15,-1,-1):
				if new[i] == 0:
					continue
				if i%4 != 0:
					if new[i-1] == 0:
						new[i-1] = new[i]
						new[i] = 0
					elif new[i-1] == new[i] and i not in merged:
						new[i-1] *= 2
						new[i] = 0
						score = score + new[i-1]
						merged.append(i-1)
	
		return new

	def _render(self,mode='human', close=False):
		if close:
			return
		outfile = StringIO() if mode == 'ansi' else sys.stdout
		row = col = 4
		desc = self.matrix.tolist()
		desc = [[c.decode('utf-8') for c in line] for line in desc]
		desc[row][col] = utils.colorize(desc[row][col], "red", highlight=True)
		outfile.write("\n".join(''.join(line) for line in desc)+"\n")
		if self.lastaction is not None:
			outfile.write("  ({})\n".format(["Left", "Down", "Right", "Up"][self.lastaction]))
		else:
			outfile.write("\n")
		return outfile



					
						




					


