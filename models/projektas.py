# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Projektas(models.Model):
    _name = 'projektai.projektas'
    _description = "Projektai"

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    client_id = fields.Many2one('res.partner', string="Client")
    employees_ids = fields.Many2many('hr.employee', string="Employees")
    darbai_ids = fields.One2many('projektai.darbas', 'projektas_id', string="Works")
    saskaitos_ids = fields.One2many('projektai.saskaita', 'projektas_id', string="Sąskaitos")

    employees_percentage = fields.Float('Employees percentage', compute='_get_employees_percentage')

    status = fields.Selection([
        ('draft', "Draft"),
        ('started', "Started"),
        ('done', "Done"),
    ], string="Progress", default='draft', translate=True)
    color = fields.Integer()

    employees_count = fields.Integer(
        string="Employees count", compute='_get_employees_count', store=True)

    @api.depends('employees_ids')
    def _get_employees_percentage(self):
        total_len = self.env['hr.employee'].search_count([])
        for r in self:
            r.employees_percentage = (len(r.employees_ids) / total_len) * 100.0


    @api.depends('employees_ids.name')
    def _get_employees_count(self):
        for r in self:
            r.employees_count = len(r.employees_ids)
            print(f"DN: {r.employees_count}")

    def send_info(self):
        template = self.env.ref('projektai.project_info_mail_template')
        self.env['mail.template'].browse(template.id).send_mail(self.id)
        print("Išsiųsta")