#!/usr/bin/python
from __future__ import unicode_literals

from general_classes import Creature
from general_classes import Object
from specific_classes import Lion


def wait():
    raw_input('\nPress Enter to continue...\n\n')


def create_an_object():
    my_object_properties = {
        'name': 'creature',
    }

    object = Object()

    object.set_properties(my_object_properties)
    object.print_properties()

    wait()


def create_a_creature():
    my_creature_properties = {
        'name': 'Lion',
        'mass': '225 kg',
        'classification': 'animal',
    }
    creature = Creature()

    creature.set_properties(my_creature_properties)
    creature.print_properties()

    wait()


def create_a_lion():
    my_lion_properties = {
        'name': 'Lion',
        'mass': '225 kg',
        'classification': 'animal',
    }
    my_lion_taxonomy = {
        'Domain': 'Eukaryote',
        'Kingdom': 'Animalia',
        'Phylum': 'Chordata',
        'Class': 'Mammalia',
        'Order': 'Carnivora',
        'Family': 'Felidae',
        'Genus': 'Panthera',
        'Species': 'Panthera leo',
    }

    lion = Lion()

    lion.set_properties(my_lion_properties)
    lion.set_taxonomy(my_lion_taxonomy)

    lion.print_properties()
    wait()

    lion.print_taxonomy()
    wait()

    lion.print_all_properties()
    wait()


if __name__ == '__main__':
    wait()
    # How to instantiate and use classes
    create_an_object()
    create_a_creature()
    create_a_lion()
