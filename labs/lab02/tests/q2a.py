OK_FORMAT=True
test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> prevalences = [0.001, 0.01, 0.1]\n'
                                               '>>> sensitivities = [1, 0.95, 0.9, 0.8]\n'
                                               '>>> specificities = [1, 0.99, 0.95, 0.9]\n'
                                               '>>> inputs = list(itertools.product(prevalences, sensitivities, specificities))\n'
                                               '>>> outputs = [compute_posterior_probability(*inp) for inp in inputs]\n'
                                               '>>> \n'
                                               ">>> hash_list = ['e4c2e8edac362acab7123654b9e73432','02d032eccec8949f6af6e04e6cdd3a8d',\n"
                                               "...  '0d16a6cb2ca34d65da949608a7bc01d1','04817efd11c15364a6ec239780038862',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','fdfff99d8a4957f3fccd95640f0a42e6',\n"
                                               "...  '9535d704a247fcd285782be1c551ecbd','45e6e163a7efd52d15f22976ec0f69a5',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','9068cf4574981fea8addf5d891282c1b',\n"
                                               "...  '4d861ace718e35d16925a986b74e459f','45e6e163a7efd52d15f22976ec0f69a5',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','93cf3ca031fd3a5694d40fc4c0a2d0b0',\n"
                                               "...  'ba4b140343c1a0b1ad0dd842f6b6a4f6','e0d088d01b309e29e7e12e7b657d04c6',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','a7473b0d7fc57e553ee66811867c7c5a',\n"
                                               "...  'c61adf9c548ef03bc82f1758a5290f50','052fbf0fbad7b4a752d34e1dc0e76cfa',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','ab01272978f4106a12ede6fe2a850be4',\n"
                                               "...  '924df509ef4290478c98958694da991e','3733db24881f3632a5c68823d705077c',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','9e89f1ca90178f2aba46ef74daf55f2e',\n"
                                               "...  'c119c1e8ac146629b48d7e173155659d','9068cf4574981fea8addf5d891282c1b',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','66bf30c49ea8026353fd6b17fc915dab',\n"
                                               "...  '711ad51d1d8b437c5425ca486f7e4d3c','8afae07169cd20be8708f022eec2ca75',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','277a3442230767b6c34ff69f1caafbfa',\n"
                                               "...  '2ecbf51392f8c6f3ea44bd7fc2b00efc','061dcd6671866898f6104fdc9ee4907d',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','ac9ded11a9d24e0a4098f94ef04d5bd5',\n"
                                               "...  '33a9cca7782132c27407c8afff0e533a','4181aff438aab51cc6bd64da498f3f24',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','4d94e4ce9554bd92202036432dcd774c',\n"
                                               "...  '27df4064836a51dbcd313df8d81e02ed','d310cb367d993fb6fb584b198a2fd72c',\n"
                                               "...  'e4c2e8edac362acab7123654b9e73432','a6fb83d730a6b986b3d7715c97485cdd',\n"
                                               "...  '100dd920921e3c509b9afd9dff04f149','b18a4559a7442eb1c25d3fb936e0a159']\n"
                                               '>>> np.all( [get_hash(outputs[i]) == hash_list[i] for i in range(len(outputs))] ) \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
