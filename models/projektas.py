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

    def send_info(self):
        print("Veikia")
        # Find the e-mail template
        # template = self.env.ref('wind_turbine.project_stage1_mail_template')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('send_mail_template_demo', 'example_email_template')

        # template.write({'attachment_ids': [(6, 0, self.wt_documents)]})

        # for slf in self:
        #     if slf.park_plan:
        #         attachment = {
        #             'name': str(slf.park_plan_filename),
        #             'datas': slf.park_plan,
        #             'datas_fname': str(slf.park_plan_filename),
        #             'res_model': 'wind_turbine.project',
        #             'type': 'binary'
        #         }
        #
        #         id = self.env['ir.attachment'].create(attachment)
        #         template.attachment_ids = [(4, id.id)]
        #
        #     for one_doc in slf.wt_documents:
        #         attachment = {
        #             'name': str(one_doc.name),
        #             'datas': one_doc.file,
        #             'datas_fname': str(one_doc.name),
        #             'res_model': 'wind_turbine.project',
        #             'type': 'binary'
        #         }
        #
        #         id = self.env['ir.attachment'].create(attachment)
        #         template.attachment_ids = [(4, id.id)]
        #
        #     if slf.turbine_type:
        #         for turbine_doc in slf.turbine_type.turbine_documents:
        #             attachment = {
        #                 'name': str(turbine_doc.name),
        #                 'datas': turbine_doc.file,
        #                 'datas_fname': str(turbine_doc.name),
        #                 'res_model': 'wind_turbine.turbine',
        #                 'type': 'binary'
        #             }
        #
        #             id = self.env['ir.attachment'].create(attachment)
        #             template.attachment_ids = [(4, id.id)]
        #
        #     # Send out the e-mail template to the user
        #     self.env['mail.template'].browse(template.id).send_mail(self.id)
        #
        #     counter = 0
        #
        #     for one_doc in slf.wt_documents:
        #         template.attachment_ids = [(3, id.id - counter)]
        #         counter += 1
        #
        #     if slf.turbine_type:
        #         for turbine_doc in slf.turbine_type.turbine_documents:
        #             template.attachment_ids = [(3, id.id - counter)]
        #             counter += 1
        #
        #     if slf.park_plan:
        #         template.attachment_ids = [(3, id.id - counter)]
