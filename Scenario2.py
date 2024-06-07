#Thabang Sambo
#5 May 2024
#RL assignment

from FourRooms import FourRooms
import numpy as np

#four rooms class
class FourRooms(FourRooms):
#set up four rooms enviroment
    def __init__(self, stochastic=True, learning_rate=0.1, discount_factor=0.94, epsilon=0.2):
        super().__init__('multi', stochastic)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        # initialize table enviroment
        self.Qtable = np.zeros((11, 11, 4))  

#frequently record q table and improve and update values
    def improve_Qtable(self, state, act, reward, next_state):
        prev_Qtable_value = self.Qtable[state[1] - 1, state[0] - 1, act]
        next_maxQvalue = np.max(self.Qtable[next_state[1] - 1, next_state[0] - 1])
        updated_Qtable_value = prev_Qtable_value + self.learning_rate * (reward + self.discount_factor * next_maxQvalue - prev_Qtable_value)
        self.Qtable[state[1] - 1, state[0] - 1, act] = updated_Qtable_value

#choose actions here
    def agent_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice([FourRooms.UP, FourRooms.DOWN, FourRooms.LEFT, FourRooms.RIGHT])
        else:
            return np.argmax(self.Qtable[state[1] - 1, state[0] - 1])

#train agent with reward packages
    def train(self, num_episodes):
        for episode in range(num_episodes):
            self.newEpoch()
            while not self.isTerminal():
                state = self.getPosition()
                act = self.agent_action(state)
                gridType, newPos, packagesRemaining, isTerminal = self.takeAction(act)
                #give agent a reward of 1 if not give nothing
                reward = 1 if gridType > 0 else 0  
                self.improve_Qtable(state, act, reward, newPos)

#test agent knowledge of enviroment
    def test(self):
        self.newEpoch()
        while not self.isTerminal():
            state = self.getPosition()
            act = np.argmax(self.Qtable[state[1] - 1, state[0] - 1])
            gridType, newPos, packagesRemaining, isTerminal = self.takeAction(act)
            print("Agent took act {} and moved to {} of type {}".format(['UP', 'DOWN', 'LEFT', 'RIGHT'][act], newPos, ['EMPTY', 'RED', 'GREEN', 'BLUE'][gridType]))

#main
def main():
#create four rooms object
    fourRoomsObj = FourRooms()
    #define the number of training episodes
    fourRoomsObj.train(num_episodes=1000)
    #test
    fourRoomsObj.test()
    #show image after execution
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()
