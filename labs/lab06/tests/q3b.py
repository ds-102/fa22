OK_FORMAT=True
test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> checks = [coefficient_df.shape == (12, 2),\n'
                                               "...           coefficient_df['feature'][0] == 'x1',\n"
                                               "...           coefficient_df['feature'][1] == 'x2']\n"
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
