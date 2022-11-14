OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> env = GridWorld([["R", "100"],\n'
                                               '...                  ["", "100"],\n'
                                               '...                  ["100", "X"]], stochastic=False)\n'
                                               '>>> \n'
                                               ">>> Qopt = { (0, 0): {'north': 90, 'west': 90,'east': 100,'south': 90},\n"
                                               "...          (0, 1): {'north': 0, 'west': 0, 'east': 0,'south': 0},\n"
                                               "...          (1, 0): {'north': 90, 'west': 90, 'east': 100,'south': 100},\n"
                                               "...          (1, 1): {'north': 0, 'west': 0, 'east': 0, 'south': 0},\n"
                                               "...          (2, 0): {'north': 0, 'west': 0, 'east': 0, 'south': 0},\n"
                                               "...          (2, 1): {'north': 0, 'west': 0, 'east': 0, 'south': 0} }\n"
                                               '>>> \n'
                                               ">>> checks = [greedy_action((1,0), Qopt) == ['east', 'south'],\n"
                                               "...           greedy_action((0,0), Qopt) == ['east']]\n"
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
