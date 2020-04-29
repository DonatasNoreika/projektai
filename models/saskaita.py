from odoo import models, fields, api, exceptions, _


class Saskaita(models.Model):
    _name = 'projektai.saskaita'
    _description = "Sąskaitos"

    number = fields.Char(string="Number", required=True)
    client_id = fields.Many2one('res.partner', string="Client")
    projektas_id = fields.Many2one('projektai.projektas', string="Project")
    eilutes_ids = fields.One2many('projektai.eilute', 'saskaita_id', string="Darbai")
    status = fields.Selection([
        ('draft', "Draft"),
        ('sent', "Sent"),
        ('paid', "Paid"),
    ], string="Progress", default='draft', translate=True)


class SaskaitaEilute(models.Model):
    _name = 'projektai.eilute'
    _description = "Sąskaitos eilutės"

    saskaita_id = fields.Many2one('projektai.saskaita', string="Invoice")
    darbas_id = fields.Many2one('projektai.darbas', string="Work")
    price = fields.Float(string="Price")

    # client_id = fields.Many2one('res.partner', string="Client")
    # projektas_id = fields.Many2one('projektai.projektas', string="Project")
