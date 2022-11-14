OK_FORMAT=True
test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(20)\n'
                                               '>>> test_samples = run_policy(random_policy, simple_env, False)\n'
                                               '>>> value = calculate_return(test_samples)\n'
                                               ">>> get_hash(value) == '9b3beb889e50e2b12746d10f923935dc'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
