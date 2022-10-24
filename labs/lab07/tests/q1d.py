OK_FORMAT=True
test = {   'name': 'q1d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> betas = betas_model.params\n>>> checks = [np.abs(betas[0]-5)< 0.1,\n...           np.abs(betas[1]-12)< 0.1]\n>>> np.all(checks)\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
