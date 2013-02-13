from __future__ import unicode_literals

from general_classes import Creature
from general_classes import Taxonomy

class Lion(Creature, Taxonomy):
    def __init__(self):
        self.properties = {
            'name': '',
            'mass': '',
            'classification': '',
            }

        self.taxonomy = {
            'Domain': '',
            'Kingom': '',
            'Phylum': '',
            'Class': '',
            'Order': '',
            'Family': '',
            'Genus': '',
            'Species': '',
            }

    def print_all_properties(self):
        for key in self.properties:
            print '{0} - {1}'.format(key, self.properties[key])

        for key in self.taxonomy:
            print '{0} - {1}'.format(key, self.taxonomy[key])

