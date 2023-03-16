# -*- coding: utf-8 -*-

from odoo import fields, models


class PetAllergicToMedications(models.Model):
    _name = 'pet.allergic.to.medications'
    _description = 'Pet Allergic To Medications'

    medical_history_id = fields.Many2one(string="Medical History", comodel_name="pet.medical.history")
    pet_id = fields.Many2one(string="Pet", comodel_name="pet.pet")
    name = fields.Char(string="Name")
    side_efflects = fields.Char(string="Side Effects")