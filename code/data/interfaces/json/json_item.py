from data.vulnerability_item import VulnerabilityItem


class JsonItem(VulnerabilityItem):
    probability = ""
    cvvs_base_score = ""
    name = ""
    type = ""
    description = ""
    last_detected_at = ""
    id=""

    def __init__(self, data_dictionary):
        self.probability = data_dictionary['probability']
        self.cvvs_base_score = data_dictionary['cvss_base_score']
        self.name = data_dictionary['title']
        self.type = data_dictionary['type']
        self.description = data_dictionary['description']
        self.last_detected_at = data_dictionary['last_detected_at']
        self.id = data_dictionary['_id']

        print("Item created. Name {}. Probability: {}. Base score: {}".format(self.name, self.probability, self.cvvs_base_score))

    def we_should_get_items_via_methods_instead(self):
        pass