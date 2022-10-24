OK_FORMAT=True
test = {   'name': 'q3ai',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> params = gamma1_model.params\n'
                                               '>>> checks = [len(params)==2,\n'
                                               '...          np.abs(params[0] - 50.16)<0.5,\n'
                                               '...          np.abs(params[1] - 1)<0.1]\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
