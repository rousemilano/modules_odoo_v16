# -*- coding: utf-8 -*-

from odoo import fields, models

class PetType(models.Model):
    _name = 'pet.type'
    _description = 'Pet Type'

    name = fields.Char(string="Name")
