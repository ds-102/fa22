OK_FORMAT=True
test = {   'name': 'q2d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> k_factors = [0, 10, 100]\n'
                                               '>>> posterior_probabilities = [0.1, 0.5, 0.9]\n'
                                               '>>> inputs= list(itertools.product(posterior_probabilities, k_factors))\n'
                                               '>>> outputs = [make_decision(*inp) for i, inp in enumerate(inputs)]\n'
                                               '>>> \n'
                                               ">>> hash_list = ['cfcd208495d565ef66e7dff9f98764da', 'c4ca4238a0b923820dcc509a6f75849b',\n"
                                               "...              'c4ca4238a0b923820dcc509a6f75849b', 'cfcd208495d565ef66e7dff9f98764da',\n"
                                               "...              'c4ca4238a0b923820dcc509a6f75849b', 'c4ca4238a0b923820dcc509a6f75849b',\n"
                                               "...              'cfcd208495d565ef66e7dff9f98764da', 'c4ca4238a0b923820dcc509a6f75849b',\n"
                                               "...              'c4ca4238a0b923820dcc509a6f75849b']\n"
                                               '>>> np.all( [get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs))] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
