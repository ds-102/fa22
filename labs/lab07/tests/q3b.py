OK_FORMAT=True
test = {   'name': 'q3b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> params = beta1_model.params\n'
                                               '>>> checks = [len(params)==2,\n'
                                               '...          np.abs(params[0] - 612)<5,\n'
                                               '...          np.abs(params[1] - 4.84)<0.3]\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
