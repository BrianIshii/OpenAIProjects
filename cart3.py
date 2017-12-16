import gym
#position of cart, velocity of cart, angle of pole, rotation rate of pole
#0 left 1 right
bestReward = 0
allTotalReward = 0
env = gym.make('CartPole-v0')
#print(env.observation_space)
#print(env.action_space)
#print(env.observation_space.high)
#print(env.observation_space.low)
for i_episode in range(20):
    observation = env.reset()
    totalReward = 0
    for t in range(400):
        env.render()
        if (observation[1] > 0):
            if (observation[2] >= .050):
                action = 1
            else:
                action = 0
        else:
            if (observation[2] <= -.050):
                action = 0
            else:
                action = 1
        if observation[0] < -2.2:
            action = 1
        if observation[0] > 2.2:
            action = 0
        #print("action: " + str(action) +" obs: " + str(observation))
        observation, reward, done, info = env.step(action)
        totalReward += reward
        #print("done? " + str(done))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("reward: " + str(totalReward))
            if (totalReward > bestReward):
                bestReward = totalReward
            allTotalReward += totalReward
            break
    if not done:
        print("win")
        allTotalReward += totalReward
print(str(bestReward))
print(str(allTotalReward / 20))
