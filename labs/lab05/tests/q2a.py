OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> x_values = [10, 15, 20, 25, 30, 35]\n'
                                               '>>> h_values = [0.5, 1, 2, 5, 10]\n'
                                               '>>> inputs = list(itertools.product(x_values, h_values))\n'
                                               '>>> outputs = [p_hat(*inp, X_observed) for inp in inputs]\n'
                                               ">>> hash_list = ['bfde2cf30f9e9ce79408d99cab3e8bc8', '0574a27738923dd052ed0b873c176afc', '78b6d148d48bbea1345c899ca9e46909', \n"
                                               "...  'f4ee6417f4b3ac1be9eb6568e73144b6', '3ffdc10d8a61ad159f223313dfbc03e2', '605849c8f83de4da7c6fd144d7f58826', \n"
                                               "...  '3f372d09d37f32da442cb9ee0ac460f0', '5b3bc4848902c9a21de80767f9e339b8', '71c61135ff01aa84ee86864b86711f5b', \n"
                                               "...  '04d8f0e70a01305f62dbadaa76a8f7cb', '45bd1e472af7b3bc57dc9312833c17a0', '45367152f5d7346868703d4980f60e03', \n"
                                               "...  '27e795eb0f314edf0479737480ab0f2a', 'd16aea76e1e1217b7eb5f7395948d364', 'd9cd4af75fe14d77a6faa0335f83b8c0', \n"
                                               "...  '2f6f54bd4207339ea29d730563c34b14', '2e0bfa827d51449a197fae6ab9f4804c', 'e0e4a546725d40f259b552ae41932f38', \n"
                                               "...  'ee15c394e25320ba6ce793eeaef72cdb', '9740966b3dc9d6fd0efba0313c963536', '30565a8911a6bb487e3745c0ea3c8224', \n"
                                               "...  '7f77a1b9954bf3ae6f43c6298871aeda', 'e5b43ca16f1f9cf6cbcfa71cdc7220ae', '83441ddfbbdcf553b5efe63b81eb1832', \n"
                                               "...  '2a6b856fad8c51aed13cfd58c948b380', '3b15219be5ebd7c0831dc46746a52d3c', '870b8425c55942fe40463327364cb546', \n"
                                               "...  'a2eb92865432da0c58cef552428f4ed1', 'dfff58ed1f9b7657068b28b69b62d70e', 'ee217454afa3c02cb3f1799b5aad3608']\n"
                                               '>>> \n'
                                               '>>> checks = [get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs))]\n'
                                               '>>> np.all(checks)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
