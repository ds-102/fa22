OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> logger.setLevel(logging.ERROR)\n'
                                               '>>> model, trace = approximate_inference_MCMC(10, 20)\n'
                                               ">>> thetas = trace['theta']\n"
                                               '>>> logger.setLevel(logging.INFO)\n'
                                               '>>> thetas.shape == (2000,12)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
