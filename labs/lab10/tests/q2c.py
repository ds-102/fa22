OK_FORMAT=True
test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(0)\n'
                                               '>>> env_test = GridWorld([["R", "", "100",  "X", ],\n'
                                               '...                       ["", "X", "X", "X"],\n'
                                               '...                       ["", "", "",  "100"]], stochastic=False)\n'
                                               '>>> Q_values_test = init_Q(env_test)\n'
                                               '>>> Q_values_test = run_agent(Q_values_test, env_test, 1000, alpha=0.5, render=False) \n'
                                               ">>> output_test = {(0, 0): {'north': 3.345, 'west': 5.017, 'east': 0.0, 'south': 65.610},\n"
                                               "...                (0, 1): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (0, 2): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (0, 3): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (1, 0): {'north': 3.345, 'west': 8.458,'east': 3.075,'south': 72.9},\n"
                                               "...                (1, 1): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (1, 2): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (1, 3): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0},\n"
                                               "...                (2, 0): {'north': 6.664,'west': 12.530,'east': 81.0, 'south': 12.530},\n"
                                               "...                (2, 1): {'north': 22.781, 'west': 4.556, 'east': 90.0, 'south': 25.313},\n"
                                               "...                (2, 2): {'north': 43.594, 'west': 20.25, 'east': 100.0, 'south': 33.75},\n"
                                               "...                (2, 3): {'north': 0.0, 'west': 0.0, 'east': 0.0, 'south': 0.0}}\n"
                                               '>>> checks = []\n'
                                               '>>> for state, state_dict in Q_values_test.items():\n'
                                               '...     for action, q_val in state_dict.items():\n'
                                               '...         checks.append(np.abs(q_val - output_test[state][action])  < 0.01)\n'
                                               '...         \n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
