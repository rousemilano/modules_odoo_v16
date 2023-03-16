# -*- coding: utf-8 -*-

{
    'name': 'Pet',
    'version': '1.0',
    'description': 'Is a module for manager pet in a clinic of pet',
    'category': 'Hidden',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pet_breed.xml',
        'views/pet_menuitem.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}