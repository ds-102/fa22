OK_FORMAT=True
test = {   'name': 'q1c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> alpha_values = [0.05, 0.1, 0.2, 0.4]\n'
                                               '>>> k_factors = [0, 10, 100]\n'
                                               '>>> inputs = list(itertools.product(alpha_values, k_factors))\n'
                                               '>>> outputs = [compute_alpha_average_loss(p_values, reality, *inp) for inp in inputs]\n'
                                               '>>> \n'
                                               ">>> hash_list = ['8d0a5f87d0563079e70969b527b22b2c', '1370c7dde8b12484e1f9f3376ec72693', \n"
                                               "...              'f106401a6d5ceaa1a89d99bcc773f8db', 'd92f2ab695c640d68b7b0f055704d892', \n"
                                               "...              '066517035812371facdef5f27ff5c7c9', '91709ca4894f058b311f697527479564', \n"
                                               "...              '49f12f9c625759e7bb9e3f2fe5cee530', '38888496421ef7c75527678f1e718c19', \n"
                                               "...              '701a4e33513e8e55f91eac027a42b6fe', 'a6107b1736a62ac0c1c79546cc4ec85f', \n"
                                               "...              'd1d940b705c4e66fc40cd8ea1c2f7c57', 'a57b99387860e7d6b6de25ea47201a0b']\n"
                                               '>>> np.all( [get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs))] )\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
