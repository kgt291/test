import numpy as np
import random
from collections import defaultdict
from environment import Env


class SARSAgent:
    def __init__(self, actions):
        self.actions = actions
        self.epsilon = 0.1
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.q_table = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0]) # 상하좌우 큐값
    
    # <s, a, r, s', a'>의 샘플로부터 큐함수를 업데이트
    def learn(self, state, action, reward, next_state, next_action):
        cur_q = self.q_table[state][action]
        next_q = self.q_table[next_state][next_action]
        new_q = cur_q + self.learning_rate * (reward + self.discount_factor*next_q - cur_q)
        self.q_table[state][action] = new_q
        
    # 입실론 탐욕 정책에 따라서 행동을 반환
    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else :
            return self.arg_max(self.q_table[state])

    @staticmethod
    def arg_max(state_action):
        max_index_list = []
        max_value = state_action[0]
        for index, value in enumerate(state_action):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)

if __name__ == "__main__":
    env = Env()
    agent = SARSAgent(actions=list(range(env.n_actions)))

    for episode in range(1000):
        # 게임 환경과 상태를 초기화
        state = env.reset()
        # 현재 상태에 대한 행동을 선택
        action = agent.get_action(str(state))
        while True:
            env.render()

            # 행동을 위한 후 다음상태 보상 에피소드의 종료 여부를 받아옴
            next_state, reward, done = env.step(action)

            # 다음 상태에서의 다음 행동 선택
            next_action = agent.get_action(str(next_state))

            # <s,a,r,s',a'>로 큐함수를 업데이트
            agent.learn(str(state), action, reward, str(next_state), next_action)
            
            # 모든 큐함수를 화면에 표시
            env.print_value_all(agent.q_table)

            state = next_state
            action = next_action
            if done:
                break

