# -*- coding: utf-8 -*-

from odoo import fields, models


class PetPet(models.Model):
    _name = 'pet.pet'
    _description = 'Pet'

    name = fields.Char(string="Name")
    birth_date = fields.Datetime(string="Birth Date")
    pet_breed_id = fields.Many2one(string="Pet Breed", comodel_name="pet.breed")
    pet_type = fields.Many2one(string="Pet Type", related='pet_breed_id.pet_type_id')
    pet_owner_id = fields.Many2one(string="Pet Owner", comodel_name="res.partner")
    pet_diagnosis_ids = fields.Many2many(string="Pet Diagnosis", comodel_name="pet.diagnosis") 
    pet_allergic_to_medications_ids = fields.Many2many(string="Pet Allergic to Medications", comodel_name="pet.allergic.to.medications") 