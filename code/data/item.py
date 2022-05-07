class VulnerabilityItem:
    probability = None
    cvvs_base_score = None

    def __init__(self, data_dictionary):
        self.probability = data_dictionary['probability']
        self.cvvs_base_score = data_dictionary['cvss_base_score']

        print("Item created. Probability: {}. Base score: {}".format(self.probability, self.cvvs_base_score))