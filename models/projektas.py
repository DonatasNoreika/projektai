# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Projektas(models.Model):
    _name = 'projektai.projektas'
    _description = "Projektai"

    name = fields.Char(string="Pavadinimas", required=True)
