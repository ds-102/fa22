OK_FORMAT=True
test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> old_state_test = (1,1)\n'
                                               ">>> action_test = 'west'\n"
                                               '>>> new_state_test = (1,2)\n'
                                               ">>> Q_values_test = {(0, 0): {'north': 10.2, 'west': 8.3, 'east': -5.0, 'south': 8.1},\n"
                                               "...                  (0, 1): {'north': 8.2, 'west': -4.2, 'east': -7.7, 'south': 20.1},\n"
                                               "...                  (0, 2): {'north': 16.6, 'west': 27.9, 'east': 19.5, 'south': 13.3},\n"
                                               "...                  (0, 3): {'north': -2.0, 'west': 3.4, 'east': -2.4, 'south': 0.9},\n"
                                               "...                  (0, 4): {'north': 0.6, 'west': -3.9, 'east': 16.3, 'south': 12.5},\n"
                                               "...                  (1, 0): {'north': 25.9, 'west': 20.4, 'east': -5.2, 'south': -5.0},\n"
                                               "...                  (1, 1): {'north': 9.6, 'west': 38.5, 'east': 5.2, 'south': 8.7},\n"
                                               "...                  (1, 2): {'north': 6.7, 'west': 18.4, 'east': 12.3, 'south': 28.8},\n"
                                               "...                  (1, 3): {'north': -4.8, 'west': 24.9, 'east': 3.9, 'south': 14.4},\n"
                                               "...                  (1, 4): {'north': 25.1, 'west': 21.6, 'east': 14.6, 'south': 16.4},\n"
                                               "...                  (2, 0): {'north': 11.0, 'west': 21.9, 'east': 2.1, 'south': -4.1},\n"
                                               "...                  (2, 1): {'north': 10.9, 'west': 10.9, 'east': 11.3, 'south': 15.0},\n"
                                               "...                  (2, 2): {'north': 19.2, 'west': 13.6, 'east': 2.7, 'south': -0.6},\n"
                                               "...                  (2, 3): {'north': 7.2, 'west': 16.1, 'east': 3.2, 'south': 2.1},\n"
                                               "...                  (2, 4): {'north': 10.9, 'west': 19.7, 'east': 19.4, 'south': -6.1}}\n"
                                               '>>> reward_test_list = [-10, 0, 10, 100]\n'
                                               '>>> output_test = [34.465, 35.965, 37.465, 50.965]\n'
                                               '>>> checks = []\n'
                                               '>>> for i,reward_test in enumerate(reward_test_list):\n'
                                               '...     updated_Q_values_test = update_Q(copy.deepcopy(Q_values_test), old_state_test, action_test, \n'
                                               '...                                      new_state_test, reward_test, 0.75, 0.15)\n'
                                               '...     cur_out = updated_Q_values_test[old_state_test][action_test] \n'
                                               '...     checks.append(np.abs(output_test[i]-cur_out)<0.01)\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
