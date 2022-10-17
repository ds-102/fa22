OK_FORMAT=True
test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> checks = [get_hash(train.iloc[:,:6]) == '93f897c99882bbc06bcd6faa779cc6d3',\n"
                                               "...           get_hash(test.iloc[:,:6]) == '7382e376c3ee239052f41ac438f1b00b']\n"
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
