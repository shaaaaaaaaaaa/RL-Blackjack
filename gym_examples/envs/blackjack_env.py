# 导入必要的库
import gymnasium as gym
from gymnasium import spaces
import numpy as np

# 定义一个新的类BlackjackEnv，继承自gym.Env，表示自定义的Blackjack环境
class BlackjackEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)  # 定义动作空间：(1)要牌（twist）：玩家要多一张牌（2）停牌（stick）：玩家不要求额外的牌， 之后不再做出行动
        self.observation_space = spaces.Tuple(( # 定义观察空间，这是一个元组空间，包括三个部分
            spaces.Discrete(32),  # 玩家手牌点数 (12-31),尽管一般在12-21之间，但随着游戏进行，玩家的手牌点数可能增加使得超过21
            spaces.Discrete(11),  # 庄家明牌点数(1-10),初始化被设置为1-10之间的随机整数
            spaces.Discrete(2)    # 是否有 Useable Ace (0, 1)
        ))
        self.reset()

    def reset(self):
        self.player_sum = np.random.randint(12, 22)
        self.dealer_card = np.random.randint(1, 11)
        self.useable_ace = np.random.choice([0, 1])
        return (self.player_sum, self.dealer_card, self.useable_ace), {}

    def step(self, action):
        if action == 0:  # 停牌
            done = True
            reward = np.random.choice([1, -1])  # 随机结果
        else:  # 要牌
            self.player_sum += np.random.randint(1, 11)
            if self.player_sum > 21:
                done = True
                reward = -1
            else:
                done = False
                reward = 0
        return (self.player_sum, self.dealer_card, self.useable_ace), reward, done, False, {}

    def render(self, mode="human"):
        pass
