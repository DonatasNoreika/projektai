# -*- coding: utf-8 -*-
from odoo import fields, models

class Employee(models.Model):
    _inherit = 'hr.employee'

    # Add a new column to the res.partner model, by default partners are not
    # instructors

    project_ids = fields.Many2many('projektai.projektas',
        string="Projects")