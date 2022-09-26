OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> N = 100\n'
                                               '>>> output = get_2D_Gibbs_samples(N, 1, 1)\n'
                                               ">>> tests = [get_hash(len(output)) == 'c81e728d9d4c2f636f067f89cc14862c',\n"
                                               "...     get_hash(len(output[0])) == 'f899139df5e1059396431415e770c6dd',\n"
                                               "...     get_hash(len(output[0][0])) == 'c81e728d9d4c2f636f067f89cc14862c',\n"
                                               '...     np.abs(410-output[1]) < 100]\n'
                                               '>>> np.all(tests)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
