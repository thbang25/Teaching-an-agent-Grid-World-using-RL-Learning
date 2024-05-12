# RL_Qlearning

This repository includes an implementation of a simple grid-world environment called Four Rooms. In this environment, an agent navigates through a 2D grid with four rooms, collecting packages marked with different colors.

There are four files in the repository:

1. `FourRooms.py`: This file contains the implementation of the FourRooms class, which represents the environment. It includes methods for initializing the environment, taking action, and checking the current state of the environment.

2. `Scenario1.py`: This file demonstrates the use of a Q-learning agent to solve Scenario 1 of the Four Rooms environment. In Scenario 1, the agent must collect a single package located somewhere in the environment.

3. `Scenario2.py`: This file extends the implementation to tackle Scenario 2 of the Four Rooms environment. In Scenario 2, the agent must collect three packages located somewhere in the environment.

4. `Scenario3.py`: This file implements a Q-learning agent for solving Scenario 3 of the Four Rooms environment. In Scenario 3, the agent must collect three packages marked with different colors (red, green, and blue) in that order.

To run the program for a specific scenario, execute the corresponding Python file (`Scenario1.py`, `Scenario2.py`, or `Scenario3.py`). Make sure that all necessary files (`FourRooms.py`, `ExecutionSkeleton.py`) are in the same directory.

For example, you can use make file compilation or run each program individually using `Python Scenario1.py`.
