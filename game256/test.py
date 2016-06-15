import gym
from env2048 import *
#env = Game2048Env()
env = gym.make('FrozenLake-v0')
observation = env.reset()
print env.P
print env.isd
for _ in range(10):
	env.render()
	action = env.action_space.sample()
	a,b,c,d = env.step(action)
