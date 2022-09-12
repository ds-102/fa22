OK_FORMAT=True
test = {   
    'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> res_dict = {'TP_count': 100, 'FP_count': 20, 'TN_count':450, 'FN_count':30}\n"
                                               '>>> k_factors = [0, 10, 100]\n'
                                               '>>> avg_losses = [compute_average_loss(res_dict,k) for k in k_factors]\n'
                                               '>>> \n'
                                               ">>> hash_list = ['ab51c1986c756154d0e3feb4f5a5e829','91f25a837f3db78306b0ad2ef0437ff9','3fc1803a77013426e6707b041de152db']\n"
                                               '>>> np.all( [get_hash(avg_losses[i]) == hash_list[i] for i in range(len(k_factors))] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
