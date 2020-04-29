# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Projektas(models.Model):
    _name = 'projektai.projektas'
    _description = "Projektai"

    name = fields.Char(string="Name", required=True)
    client_id = fields.Many2one('res.partner', string="Client")
    employees_ids = fields.Many2many('hr.employee', string="Employees")
    darbai_ids = fields.One2many('projektai.darbas', 'projektas_id', string="Works")
    saskaitos_ids = fields.One2many('projektai.saskaita', 'projektas_id', string="Sąskaitos")

    employees_percentage = fields.Float('Employees percentage', compute='_get_employees_count')

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
    ], string="Progress", default='draft', translate=True)

    @api.depends('employees_ids')
    def _get_employees_count(self):
        total_len = self.env['hr.employee'].search_count([])
        for r in self:
            r.employees_percentage = (len(r.employees_ids) / total_len) * 100.0
