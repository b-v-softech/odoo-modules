# -*- coding: utf-8 -*-
from odoo import api, fields, models



class MailActivity(models.Model):
    _inherit = 'mail.activity'


    res_rec_url = fields.Char(string='Related Record', compute='_compute_res_rec_url')

    @api.depends('res_model', 'res_id')
    def _compute_res_rec_url(self):
        for activity in self:
            activity.res_rec_url = '#id=%s&model=%s' % (activity.res_id, activity.res_model)
