OK_FORMAT=True
test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Run validation tests: Do not modify\n'
                                               '>>> treatments = [0, 1]\n'
                                               '>>> k_factors = [0, 10, 100]\n'
                                               '>>> posterior_probabilities = [0.1, 0.5, 0.9]\n'
                                               '>>> inputs = list(itertools.product(treatments, posterior_probabilities, k_factors))\n'
                                               '>>> outputs = [compute_expected_loss(*inp) for i, inp in enumerate(inputs)]\n'
                                               '>>> \n'
                                               ">>> hash_list = ['30565a8911a6bb487e3745c0ea3c8224', 'e4c2e8edac362acab7123654b9e73432',\n"
                                               "...              '43a1437f7f656cd8be7c996c58719e0a', '30565a8911a6bb487e3745c0ea3c8224',\n"
                                               "...              '336669dbe720233ed5577ddf81b653d3', '88bce6f1bd04b8521f1167b5a6dec118',\n"
                                               "...              '30565a8911a6bb487e3745c0ea3c8224', 'cf5f238fca8b6e155078aa41c175743a',\n"
                                               "...              'a5efe444b4090e202d78340494947f63', 'a894124cc6d5c5c71afe060d5dde0762',\n"
                                               "...              'a894124cc6d5c5c71afe060d5dde0762', 'a894124cc6d5c5c71afe060d5dde0762',\n"
                                               "...              'd310cb367d993fb6fb584b198a2fd72c', 'd310cb367d993fb6fb584b198a2fd72c',\n"
                                               "...              'd310cb367d993fb6fb584b198a2fd72c', 'ec705edd9065ac64dc3985903df2e2e6',\n"
                                               "...              'ec705edd9065ac64dc3985903df2e2e6', 'ec705edd9065ac64dc3985903df2e2e6']\n"
                                               '>>> np.all( [get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs)) ] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
