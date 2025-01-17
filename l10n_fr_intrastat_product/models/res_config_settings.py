# Copyright 2017-2019 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    fr_intrastat_accreditation = fields.Char(
        related="company_id.fr_intrastat_accreditation", readonly=False
    )
    
    deb_per_invoice = fields.Boolean(related='company_id.deb_per_invoice', readonly=False )
