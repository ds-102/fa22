OK_FORMAT=True
test = {   'name': 'q1biii',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> checks = [((train["forest_pred"] - train["msrp"]) **2).mean() < 30000000.0,\n'
                                               '...           ((test["forest_pred"] - test["msrp"]) **2).mean() < 210000000.0,\n'
                                               '...           isinstance(forest_model, RandomForestRegressor),\n'
                                               "...           forest_model.max_features != 'auto']\n"
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
