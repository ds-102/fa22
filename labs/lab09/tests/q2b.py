OK_FORMAT=True
test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> K_test = 5\n'
                                               '>>> times_pulled_test = [3, 5, 7, 4, 1]\n'
                                               '>>> prior_means_test=[8,5,7,9,6]\n'
                                               '>>> prior_variances_test=[2.5, 0.1, 1.6, 2.3, 1.7]\n'
                                               '>>> t_test = np.sum(times_pulled_test) + 1\n'
                                               '>>> variances_test = [0.4, 0.2, 0.1, 0.2, 0.5]\n'
                                               '>>> rewards_test = [[10.4, 12.6, 11], \n'
                                               '...                 [8, 13, 12, 11, 9], \n'
                                               '...                 [9, 10, 10, 8, 9.5, 10.5, 11],\n'
                                               '...                 [8.3, 9.6, 7.9, 8.1],\n'
                                               '...                 [8]]\n'
                                               '>>> test_arm, posterior_samples_test, posterior_means_test, posterior_vars_test = TS_pull_arm(t_test, \n'
                                               '...                                                                                           variances_test, \n'
                                               '...                                                                                           times_pulled_test, \n'
                                               '...                                                                                           rewards_test,\n'
                                               '...                                                                                           prior_means_test,\n'
                                               '...                                                                                           prior_variances_test)\n'
                                               '>>> \n'
                                               '>>> checks = [test_arm == 0]\n'
                                               '>>> \n'
                                               '>>> opt_vals_means = [11.16, 9.0, 9.69, 8.49, 7.55]\n'
                                               '>>> opt_vals_vars = [0.123, 0.0286, 0.014,0.049,0.386]\n'
                                               '>>> for a in range(K_test):\n'
                                               '...     checks.append(np.abs(opt_vals_means[a] - posterior_means_test[a]) <= 0.1)\n'
                                               '...     checks.append(np.abs(opt_vals_vars[a] - posterior_vars_test[a]) <= 0.01)\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
