OK_FORMAT=True
test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> n_test_array = [10, 100, 1000]\n'
                                               '>>> x_test_array = [10, 34, 852]\n'
                                               '>>> res_array = [trivial_theta_estimate(n, x_test_array[i]) for i,n in enumerate(n_test_array)]\n'
                                               ">>> hash_list=['e4c2e8edac362acab7123654b9e73432','149dd5056939405870c9bb50cbc8691c','83659da620f470d5a131b5a9c76cfee7']\n"
                                               '>>> np.all( [get_hash(res_array[i]) == hash_list[i] for i in range(len(res_array))] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
