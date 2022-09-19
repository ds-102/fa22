OK_FORMAT=True
test = {   'name': 'q2c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> logger.setLevel(logging.ERROR)\n'
                                               '>>> nreps = 2\n'
                                               '>>> \n'
                                               '>>> hash_list = [["e85b79abfd76b7c13b1334d8d8c194a5"],\n'
                                               '...             ["261943f3a93b683ceeac658927f3923f"],\n'
                                               '...             ["149dd5056939405870c9bb50cbc8691c"],\n'
                                               '...             ["ba6197788db60f5e2cb45cd403fa6559"],\n'
                                               '...             ["246c0903b5a64b2a854ec1e7865f174f"],\n'
                                               '...             ["ffa243f771800363714f6055d9236fd6"],\n'
                                               '...             ["ffa243f771800363714f6055d9236fd6", "9f4721cf71c0ed18cd60356036b953cc"],\n'
                                               '...             ["45efc23f34e05a9ea4f5024988047dd6"],\n'
                                               '...             ["8f11bfb91ec29936603314c7cbc46119"],\n'
                                               '...             ["a3f2a910685f5b07f5f45a5fc1fdb389"],\n'
                                               '...             ["91afec64e32d6bf957e441df2ab638bb"],\n'
                                               '...             ["8ce3fac7e23a02ab4e00cf0f1e03310a"]]\n'
                                               '>>> \n'
                                               '>>> checks = []\n'
                                               '>>> for _ in range(nreps):\n'
                                               '...     posterior_estimates_test = empirical_posterior_mean_estimates(10,25) \n'
                                               '...     checks.append(np.all( [get_hash(posterior_estimates_test[i],2) in hash_list[i] for i in range(len(hash_list))] ))\n'
                                               '>>> \n'
                                               '>>> logger.setLevel(logging.INFO)\n'
                                               '>>> np.any(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
