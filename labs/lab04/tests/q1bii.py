OK_FORMAT=True
test = {   'name': 'q1bii',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> N = 5000\n'
                                               '>>> tests = [np.abs(0.075-len(get_2D_samples(N, 0.015))/N) < 0.015,\n'
                                               '...     np.abs(0.045-len(get_2D_samples(N, 0.01))/N) < 0.015]\n'
                                               '>>> np.all(tests)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
