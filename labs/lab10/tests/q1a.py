OK_FORMAT=True
test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(20)\n'
                                               '>>> test_samples = run_policy(random_policy, simple_env, False)\n'
                                               '>>> \n'
                                               ">>> checks = [test_samples[2][1] == 'south',\n"
                                               '...           test_samples[-1][3] == 100]\n'
                                               '>>> \n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
