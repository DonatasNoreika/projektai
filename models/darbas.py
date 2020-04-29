# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Darbas(models.Model):
    _name = 'projektai.darbas'
    _description = "Darbai"

    name = fields.Char(string="Name", required=True)
    projektas_id = fields.Many2one('projektai.projektas', string="Project")