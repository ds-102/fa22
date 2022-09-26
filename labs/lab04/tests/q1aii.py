OK_FORMAT=True
test = {   'name': 'q1aii',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> N = 1000\n'
                                               '>>> tests = [np.abs(1.5-np.mean(get_1D_samples(N, 1/15))) < 0.1,\n'
                                               '...     np.abs(0.3-len(get_1D_samples(N, 1/15))/N) < 0.05,\n'
                                               '...     np.abs(0.23-len(get_1D_samples(N, 1/20))/N) < 0.05,\n'
                                               '...     np.abs(0.18-len(get_1D_samples(N, 1/25))/N) < 0.05]\n'
                                               '>>> np.all(tests)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
