OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> params = beta_naive_model.params\n'
                                               '>>> checks = [len(params)==2,\n'
                                               '...          np.abs(params[0] - 42.85)<0.5,\n'
                                               '...          np.abs(params[1] - 12.96)<0.2]\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
