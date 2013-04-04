from __future__ import unicode_literals


class Object():
    def __init__(self):
        self.properties = {
            'name': '',
        }

    def set_properties(self, data):
        for key in self.properties:
            self.properties[key] = data.get(key, None)

    def print_properties(self):
        for key in self.properties:
            print '{0} - {1}'.format(key, self.properties[key])


class Creature(Object):
    def __init__(self):
        self.properties = {
            'name': '',
            'mass': '',
            'classification': '',
        }


class Taxonomy():
    def __init__(self):
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

    def set_taxonomy(self, data):
        for key in self.taxonomy:
            self.taxonomy[key] = data.get(key, None)

    def print_taxonomy(self):
        for key in self.taxonomy:
            print '{0} - {1}'.format(key, self.taxonomy[key])
