OK_FORMAT=True
test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> K_test = 5\n'
                                               '>>> times_pulled_test = [3, 5, 7, 4, 0]\n'
                                               '>>> t_test = np.sum(times_pulled_test) + 1\n'
                                               '>>> standard_deviations_test = [0.4, 0.2, 0.1, 0.2, 0.5]\n'
                                               '>>> rewards_test = [[10.4, 10.6, 11], \n'
                                               '...                 [8, 13, 12, 11, 9], \n'
                                               '...                 [9, 10, 10, 8, 9.5, 10.5, 11],\n'
                                               '...                 [8.3, 9.6, 7.9, 8.1],\n'
                                               '...                 []]\n'
                                               '>>> test_arm, test_confidence_bounds = UCB_pull_arm(t_test, standard_deviations_test, times_pulled_test, rewards_test)\n'
                                               '>>> \n'
                                               '>>> checks = [test_arm == 4, np.isinf(test_confidence_bounds[-1])]\n'
                                               '>>> opt_vals = [11.64, 10.98, 9.87, 8.90]\n'
                                               '>>> for a in range(K_test-1):\n'
                                               '...     checks.append(np.abs(opt_vals[a] - test_confidence_bounds[a]) <= 0.1)\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
