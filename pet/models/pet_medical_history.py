# -*- coding: utf-8 -*-

from odoo import fields, models


class PetMedicalHistory(models.Model):
    _name = 'pet.medical.history'
    _description = 'Pet Medical History'

    registration_date = fields.Datetime(string="Registration Date")
    state = fields.Selection([('in_process', 'In Process'), ('finish', 'Finish')], string="State", default="in_process")
    assistant_id = fields.Many2one(string="Assistant", comodel_name="res_users")
    pet_id = fields.Many2one(string="Pet", comodel_name="pet.pet")
    pet_owner_id = fields.Many2one(string="Pet Owner", related='pet_id.pet_owner_id')
    pet_diagnosis_ids = fields.Many2many(string="Pet Diagnosis", comodel_name="pet.diagnosis") 
    pet_allergic_to_medications_ids = fields.Many2many(string="Pet Allergic to Medications", comodel_name="pet.allergic.to.medications") 

