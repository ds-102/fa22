OK_FORMAT=True
test = {   'name': 'q4a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.random.seed(13)\n'
                                               '>>> Z_star, Z_bar = draw_Z_star(X_observed)\n'
                                               ">>> hash_list = ['d470a4a2eb42e8cd29b89ab69a5e6876' , 'bdffe8df0c64d512fa0542988da75dc9']\n"
                                               '>>> np.all([get_hash(Z_star[0]) == hash_list[0] , get_hash(Z_bar) == hash_list[1]])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
