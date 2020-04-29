# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Projektas(models.Model):
    _name = 'projektai.projektas'
    _description = "Projektai"

    name = fields.Char(string="Name", required=True)
    client_id = fields.Many2one('res.partner', string="Client")
    employees_ids = fields.Many2many('hr.employee', string="Employees")