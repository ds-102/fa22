OK_FORMAT=True
test = {   'name': 'q2bi',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> worst = ['6ea9ab1baa0efb9e19094440c317e21b' , '17e62166fc8586dfa4d1bc0e1742c08b']\n"
                                               '>>> checks = [get_hash(worst_forest_predicted_cars_df.index.values[0]) in worst,\n'
                                               '...           get_hash(worst_forest_predicted_cars_df.index.values[1]) in worst ]\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
