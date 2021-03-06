# -*- coding: utf-8 -*-
# © 2017 Le Filament (<http://www.le-filament.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
import odoo.addons.decimal_precision as dp

class LeFilamentProjectTask(models.Model):
    _inherit = 'project.task'

    price_subtotal = fields.Monetary(string='Subtotal initial', readonly=True, store='True')
    currency_id = fields.Many2one(related='sale_line_id.currency_id', store=True, string='Currency', readonly=True)