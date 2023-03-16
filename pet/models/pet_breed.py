# -*- coding: utf-8 -*-

from odoo import fields, models


class PetBreed(models.Model):
    _name = 'pet.breed'
    _description = 'Pet Breed'

    name = fields.Char(string="Name")
    pet_type_id = fields.Many2one(string="Pet Type", comodel_name="pet.type")