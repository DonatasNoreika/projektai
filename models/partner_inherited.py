# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    projektai_ids = fields.One2many('projektai.projektas', "client_id",
        string="Assigned Projects", readonly=True)