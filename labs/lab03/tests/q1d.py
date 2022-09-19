OK_FORMAT=True
test = {   'name': 'q1d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> N_test = 100\n'
                                               '>>> X_test = 20\n'
                                               '>>> alpha_test_array = [1, 10, 100]\n'
                                               '>>> beta_test_array = [1, 10, 100]\n'
                                               '>>> inputs = list(itertools.product(alpha_test_array, beta_test_array))\n'
                                               '>>> outputs = [posterior_mean_estimate(N_test, X_test, *inp) for inp in inputs]\n'
                                               ">>> hash_list = ['8ae3cf8f9366cbdea2ccf7706546ba4a','f8ddc3234c0a54e55b01384bcfb23f90','82589ee1f18a2e0b9fe9d14836983102',\n"
                                               "...              '08cf5a2033e7e21ec90b6707c24facaf','70da82175ec8a195a3d8b0fa8f69681d','ced20bed08ecfba035cbc3e06657cff2',\n"
                                               "...              'c8a7feeaced214c662a999d9bf075e8c','790abc5c38e7c740420b03c24fabb05b','54fbf38cf649866815e0fefc46a1f6c7']\n"
                                               '>>> \n'
                                               '>>> np.all( [ get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs))] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
