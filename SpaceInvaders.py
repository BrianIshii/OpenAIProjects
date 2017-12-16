import gym
env = gym.make('SpaceInvaders-v0')
env.reset()

while True:
    action = 1 
    obs, reward, done, info = env.step(action)
    if reward > 0:
        print(reward)
        #print(obs)
    env.render()
