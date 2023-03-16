# -*- coding: utf-8 -*-

from odoo import fields, models


class PetDiagnosis(models.Model):
    _name = 'pet.diagnosis'
    _description = "Pet Diagnosis"

    name = fields.Char(string="Name")
    pet_breed_id = fields.Many2one(string="Pet Breed", comodel_name="pet.breed")
    pet_type_id = fields.Many2one(string="Pet Type", related='pet_breed_id.pet_type_id')
    pet_medical_history = fields.Many2one(string="Pet Medical History", comodel_name="pet.medical.history")
    diagnosis_type = fields.Selection([('chronic','Chronic'), ('acute', 'Acute')], string="Diagnosis Type")
    diagnosis_date = fields.Datetime(string="Diagnosis Date")

