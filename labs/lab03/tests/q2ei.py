OK_FORMAT=True
test = {   'name': 'q2ei',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> nreps = 2\n'
                                               '>>> logger.setLevel(logging.ERROR)\n'
                                               '>>> \n'
                                               ">>> hash_list = ['afbc48a7ca8d716f9efa7cc993316668',\n"
                                               "...              'e85b79abfd76b7c13b1334d8d8c194a5',\n"
                                               "...              '0bd1ed7e9617a4ed139b2f4014c7aa23',\n"
                                               "...              'afbc48a7ca8d716f9efa7cc993316668',\n"
                                               "...              '4a42799b212019a2db0b77644e33790c',\n"
                                               "...              '964e2b882801bd4ba988904454316d76',\n"
                                               "...              '964e2b882801bd4ba988904454316d76',\n"
                                               "...              '4a42799b212019a2db0b77644e33790c',\n"
                                               "...              '45efc23f34e05a9ea4f5024988047dd6',\n"
                                               "...              '451d13a5be2581a451c2284dcecddd4e',\n"
                                               "...              '2363c78ab7dba59b8443d958b47cfa2b',\n"
                                               "...              '0bd1ed7e9617a4ed139b2f4014c7aa23']\n"
                                               '>>> \n'
                                               '>>> checks = []\n'
                                               '>>> for _ in range(nreps):\n'
                                               '...     model_test, trace_test = approximate_inference_asympotmatic_MCMC(5, 10)\n'
                                               "...     post_samples_test = trace_test['theta']\n"
                                               '...     estimates = np.mean(post_samples_test, axis = 0)\n'
                                               '...     rounded_estimates = np.round(estimates / 2, 2) * 2\n'
                                               '...     checks.append(np.all( [ get_hash(rounded_estimates[i], 2) == hash_list[i] for i in range(len(hash_list))]))\n'
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
