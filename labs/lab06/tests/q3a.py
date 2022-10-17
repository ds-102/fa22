OK_FORMAT=True
test = {   'name': 'q3a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> ring_train_copy3a, ring_test_copy3a = ring_train.copy(), ring_test.copy()\n'
                                               '>>> np.random.seed(42)\n'
                                               '>>> _,_ = add_random_feature(ring_train_copy3a, ring_test_copy3a)\n'
                                               '>>> _,_ = add_random_feature(ring_train_copy3a, ring_test_copy3a)\n'
                                               ">>> checks = [get_hash(ring_train_copy3a.iloc[:,-2]) == '14ef2ae3a9fb084922404362bb715541',\n"
                                               "...           get_hash(ring_train_copy3a.iloc[:,-1]) == 'ecb3610db652a969fb1bd630e818c965']\n"
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
